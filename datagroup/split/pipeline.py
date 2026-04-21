"""
拆分工具

按一级标题 (#) 切分 Markdown 文件，再调用 LLM 提取题目为独立 md 文件
"""

import re
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from api_client import ask_ai
from system_prompts import SystemPrompts


def split_by_heading(md_content: str) -> list[tuple[str, str]]:
    """按一级标题切分内容，每个 # 标题独立生成章节"""
    heading_pattern = r'^(#\s+.+)$'
    lines = md_content.split('\n')

    sections = []
    current_heading = None
    current_content = []

    for line in lines:
        match = re.match(heading_pattern, line)
        if match:
            if current_heading is not None and current_content:
                content_str = '\n'.join(current_content).strip()
                sections.append((current_heading, content_str))

            current_heading = match.group(1).strip()
            current_content = []
        else:
            current_content.append(line)

    if current_heading is not None and current_content:
        content_str = '\n'.join(current_content).strip()
        sections.append((current_heading, content_str))

    return sections


def sanitize_filename(name: str) -> str:
    """将字符串转换为安全的文件名"""
    name = name.strip()
    name = name.replace('/', '_').replace('\\', '_')
    name = name.replace(':', '_').replace('*', '_')
    name = name.replace('?', '_').replace('"', '_')
    name = name.replace('<', '_').replace('>', '_').replace('|', '_')
    name = name.replace(' ', '_')
    if len(name) > 80:
        name = name[:80]
    return name


def stage1_split(input_file: str, output_dir: str = None) -> Path:
    """按一级标题切分 md 文件或目录，文件名编码书名"""
    input_path = Path(input_file)

    if output_dir is None:
        output_dir = input_path.parent / f"{input_path.name}_split"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    # 输入是目录：对每个 md 文件按标题切分，书名编码进文件名
    if input_path.is_dir():
        md_files = list(input_path.glob("*.md"))
        if not md_files:
            print("输入目录中未找到任何 .md 文件")
            return None

        total_sections = 0
        for md_file in sorted(md_files):
            book_name = sanitize_filename(md_file.stem)

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            sections = split_by_heading(content)
            if not sections:
                heading = content.split('\n')[0].strip() if content.split('\n') else md_file.stem
                sections = [(heading, content)]

            for heading, section_content in sections:
                total_sections += 1
                safe_heading = sanitize_filename(heading)
                output_file = output_dir / f"{total_sections:03d}@{book_name}@{safe_heading}.md"

                full_content = f"{heading}\n\n{section_content}"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(full_content)

                print(f"  [{total_sections:03d}] {heading[:50]}... -> {output_file.name}")

        print(f"[阶段 1] 从目录切分 {len(md_files)} 个文件为 {total_sections} 个章节")
        return output_dir

    # 输入是文件：书名从文件名提取
    book_name = sanitize_filename(input_path.stem)

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = split_by_heading(content)
    if not sections:
        print("未找到任何一级标题，无法切分")
        return None

    for i, (heading, section_content) in enumerate(sections, 1):
        safe_heading = sanitize_filename(heading)
        output_file = output_dir / f"{i:03d}@{book_name}@{safe_heading}.md"

        full_content = f"{heading}\n\n{section_content}"
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"  [{i:03d}] {heading[:50]}... -> {output_file.name}")

    print(f"[阶段 1] 找到 {len(sections)} 个章节")
    return output_dir


# ==================== LLM 提取题目 ====================

file_lock = threading.Lock()
problem_counter = {"count": 0}
batch_number = {"value": 1}


def extract_problem_id(first_line: str) -> str:
    """从 LLM 输出的第一行提取题号"""
    # 匹配 x.xx.xx 格式（如 1.17.35）
    m = re.match(r'^(\d+\.\d+\.\d+)', first_line)
    if m:
        return m.group(1)
    # 匹配 【数字】格式
    m = re.match(r'^【(\d+)】', first_line)
    if m:
        return m.group(1)
    # 匹配 纯数字编号（如 1. 12.）
    m = re.match(r'^(\d+)\.', first_line)
    if m:
        return m.group(1)
    # 匹配 §x.x 格式
    m = re.match(r'^§(\d+[\.\d]*)', first_line)
    if m:
        return m.group(1)
    # 匹配 No.xxx 格式
    m = re.match(r'^No\.(\d+)', first_line, re.IGNORECASE)
    if m:
        return m.group(1)
    # 匹配 (a)/(1) 小问
    m = re.search(r'\(([a-z\d]+)\)', first_line)
    if m:
        return m.group(1)
    return ""


def process_file(file_path: Path, output_dir: Path) -> int:
    """处理单个文件：调用 LLM 提取题目，每个题目保存为 {批号}_{题号}.md"""

    print(f"Processing: {file_path.name}")
    try:
        result = ask_ai(
            prompt="请从文件中提取所有题目，按指定格式输出。",
            files=str(file_path),
            system=SystemPrompts.QA_EXTRACT_TO_MD.value
        )

        # LLM 返回 NONE 表示没有题目，删除源文件并跳过
        if result.strip().upper() == 'NONE':
            try:
                file_path.unlink()
                print(f"  [{file_path.name}] 无题目，已删除")
            except Exception as e:
                print(f"  [{file_path.name}] 删除失败：{e}")
            return 0

        # 按分割线提取每道题
        blocks = re.split(r'^---$', result, flags=re.MULTILINE)
        count = 0
        for block in blocks:
            block = block.strip()
            if not block or block.upper() == 'NONE':
                continue

            lines = [l for l in block.split('\n') if l.strip()]
            if not lines:
                continue

            # 从第一行提取题号（匹配常见题号格式）
            first_line = lines[0].strip()
            problem_id = extract_problem_id(first_line)
            if not problem_id:
                # 没题号，用序号代替
                problem_id = f"unk{problem_counter['count'] + count + 1}"

            output_name = sanitize_filename(f"{batch_number['value']}_{problem_id}")
            output_file = output_dir / f"{output_name}.md"

            # 防止文件名冲突：同名文件存在时加序号后缀
            if output_file.exists():
                dup_idx = 1
                while output_file.exists():
                    dup_idx += 1
                    output_file = output_dir / f"{output_name}_{dup_idx}.md"

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(block)
            count += 1

        # 删除源文件
        try:
            file_path.unlink()
            print(f"  [{file_path.name}] 已删除")
        except Exception as e:
            print(f"  [{file_path.name}] 删除失败：{e}")

        with file_lock:
            problem_counter["count"] += count
        print(f"  [{file_path.name}] 提取 {count} 道题目")
        return count

    except Exception as e:
        print(f"  [{file_path.name}] 失败：{e}")
        return 0


def auto_batch_start(output_dir: Path) -> int:
    """从输出目录中扫描已有文件的最大批号，返回 max+1；目录不存在或无文件时返回 1"""
    if not output_dir.exists():
        return 1
    max_batch = 0
    for f in output_dir.glob("*.md"):
        parts = f.stem.split('_')
        if parts and parts[0].isdigit():
            max_batch = max(max_batch, int(parts[0]))
    return max_batch + 1 if max_batch > 0 else 1


def stage2_extract(input_dir: str, output_dir: str = None, max_workers: int = 4, batch_start: int = None) -> Path:
    """并行提取题目为单独 md 文件"""
    global problem_counter, batch_number
    problem_counter = {"count": 0}

    input_path = Path(input_dir)

    if output_dir is None:
        # 默认输出到 datagroup/question_splited
        output_dir = input_path.parent / "question_splited"
    else:
        output_dir = Path(output_dir)

    # 自动识别批号：未指定时从输出目录扫描
    if batch_start is None:
        batch_start = auto_batch_start(output_dir)

    batch_number = {"value": batch_start}
    print(f"[阶段 2] 批号起始：{batch_start}")

    output_dir.mkdir(parents=True, exist_ok=True)

    files = list(input_path.glob("*.md"))
    print(f"[阶段 2] 找到 {len(files)} 个文件，开始提取题目 (并发数：{max_workers})...")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_file, f, output_dir): f for f in files}
        for future in as_completed(futures):
            future.result()

    print(f"[阶段 2] 完成！共提取 {problem_counter['count']} 道题目")
    print(f"  输出目录：{output_dir}\n")
    return output_dir


# ==================== 主 Pipeline ====================

def run_split_pipeline(input_file: str,
                       stage1_output: str = None,
                       stage2_output: str = None,
                       max_workers: int = 4,
                       batch_start: int = None) -> Path:
    """
    运行拆分流水线：切分 → LLM提取题目

    Args:
        input_file: 输入文件路径或目录
        stage1_output: 阶段 1 输出目录（可选）
        stage2_output: 阶段 2 输出目录（可选）
        max_workers: LLM 提取并发数
        batch_start: 批号起始值。None 时自动从输出目录扫描已有最大批号+1

    Returns:
        最终输出目录路径
    """
    input_path = Path(input_file)

    print("=" * 60)
    print("题目拆分 Pipeline")
    print("=" * 60)
    print(f"输入：{input_file} ({'目录' if input_path.is_dir() else '文件'})")
    print(f"并发数：{max_workers}")
    if batch_start is not None:
        print(f"批号起始：{batch_start}（手动指定）")
    else:
        print(f"批号起始：自动检测")
    print("=" * 60 + "\n")

    # 阶段 1：按标题切分
    stage1_dir = stage1_split(input_file, stage1_output)
    if stage1_dir is None:
        raise RuntimeError("阶段 1 失败")

    # 阶段 2：LLM 提取题目
    final_dir = stage2_extract(stage1_dir, stage2_output, max_workers, batch_start)

    print("=" * 60)
    print("拆分 Pipeline 完成！")
    print(f"最终输出：{final_dir}")
    print("=" * 60)

    return final_dir


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="题目拆分 Pipeline")
    parser.add_argument("input_file", nargs="?", default="books",
                        help="输入文件路径或目录")
    parser.add_argument("-1", "--stage1-output", type=str, help="阶段 1 输出目录")
    parser.add_argument("-2", "--stage2-output", type=str, help="阶段 2 输出目录")
    parser.add_argument("-w", "--workers", type=int, default=4,
                        help="LLM 提取并发数")
    parser.add_argument("-b", "--batch-start", type=int, default=None,
                        help="批号起始值，不指定时自动从输出目录检测")

    args = parser.parse_args()

    run_split_pipeline(
        input_file=args.input_file,
        stage1_output=args.stage1_output,
        stage2_output=args.stage2_output,
        max_workers=args.workers,
        batch_start=args.batch_start,
    )