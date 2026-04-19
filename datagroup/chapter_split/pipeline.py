"""
章节拆分 Pipeline

将整书 md 文件按章节拆分，并将答案区的答案合并到对应正文章节中。
输出：每章一个 md 文件，包含正文 + 该章答案。

Pipeline:
  stage1_classify — LLM 识别章节类型 + 建立答案→章节映射
  stage2_merge — 按映射合并章节+答案，输出每章独立 md 文件
"""

import json
import re
import sys
import os
import threading
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api_client import ask_ai
from system_prompts import SystemPrompts
from split.pipeline import split_by_heading, sanitize_filename

file_lock = threading.Lock()


def _parse_llm_json(result: str) -> list[dict]:
    """从 LLM 返回中提取 JSON 数组"""
    # 尝试提取 JSON 数组
    for json_match in re.finditer(r'\[[\s\S]*?\](?:\s*$)', result):
        try:
            data = json.loads(json_match.group())
            if isinstance(data, list) and data:
                return data
        except json.JSONDecodeError:
            continue

    # 尝试提取单个 JSON 对象
    brace_positions = [m.start() for m in re.finditer(r'\{', result)]
    for start in reversed(brace_positions):
        depth = 0
        for end in range(start, len(result)):
            if result[end] == '{':
                depth += 1
            elif result[end] == '}':
                depth -= 1
            if depth == 0:
                try:
                    data = json.loads(result[start:end + 1])
                    if isinstance(data, dict):
                        return [data]
                except json.JSONDecodeError:
                    break

    return []


def _build_sections_with_lines(md_content: str) -> list[tuple[str, str, int, int]]:
    """按一级标题切分，同时记录每个章节的起止行号"""
    heading_pattern = r'^(#\s+.+)$'
    lines = md_content.split('\n')

    sections = []
    current_heading = None
    current_content = []
    start_line = 0

    for i, line in enumerate(lines):
        match = re.match(heading_pattern, line)
        if match:
            if current_heading is not None and current_content:
                content_str = '\n'.join(current_content).strip()
                sections.append((current_heading, content_str, start_line, i - 1))

            current_heading = match.group(1).strip()
            current_content = []
            start_line = i
        else:
            current_content.append(line)

    # 最后一个章节
    if current_heading is not None and current_content:
        content_str = '\n'.join(current_content).strip()
        sections.append((current_heading, content_str, start_line, len(lines) - 1))

    return sections


def _extract_answer_blocks(answer_content: str, chapter_map: dict[str, str]) -> dict[str, list[str]]:
    """按题号前缀将答案区内容分块归类到各章节"""
    result: dict[str, list[str]] = {}
    lines = answer_content.split('\n')

    current_chapter_id = None
    current_block: list[str] = []

    for line in lines:
        # 检测题号前缀（如 1.17.、2.3.、§3. 等）
        prefix_match = re.match(r'^(\d+)\.\s', line)
        if not prefix_match:
            prefix_match = re.match(r'^§(\d+)', line)
        if not prefix_match:
            prefix_match = re.match(r'^(\d+)\.\d+', line)

        if prefix_match:
            prefix_num = prefix_match.group(1) + "."
            mapped_chapter = chapter_map.get(prefix_num)

            if mapped_chapter != current_chapter_id:
                # 保存当前块
                if current_chapter_id and current_block:
                    result.setdefault(current_chapter_id, []).append('\n'.join(current_block))
                current_chapter_id = mapped_chapter
                current_block = [line]
                continue

        # 检测二级标题切换章节（如 ## Chapter II 对应的答案）
        section_match = re.match(r'^##\s+(?:Chapter|§)\s+(\w+)', line, re.IGNORECASE)
        if section_match:
            if current_chapter_id and current_block:
                result.setdefault(current_chapter_id, []).append('\n'.join(current_block))
            # 尝试从二级标题映射
            ch_num = section_match.group(1)
            current_chapter_id = None
            current_block = [line]
            continue

        if current_block or line.strip():
            current_block.append(line)

    # 保存最后一个块
    if current_chapter_id and current_block:
        result.setdefault(current_chapter_id, []).append('\n'.join(current_block))

    return result


def stage1_classify(input_file: str, output_dir: str = None, max_retries: int = 3) -> list[dict]:
    """
    阶段 1：识别章节类型 + 建立答案→章节映射

    Args:
        input_file: 整书 md 文件路径
        output_dir: 输出目录（chapter_map.json 存放位置）
        max_retries: LLM 调用重试次数

    Returns:
        章节分类映射列表
    """
    input_path = Path(input_file)
    if output_dir is None:
        output_dir = input_path.parent / "chapter_splited"
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    sections = _build_sections_with_lines(md_content)
    if not sections:
        print("[章节拆分] 未找到一级标题，无法切分")
        return []

    # 构建章节摘要发给 LLM
    book_name = sanitize_filename(input_path.stem)
    summary_lines = []
    answer_sections_indices = []

    for i, (heading, content, start_line, end_line) in enumerate(sections):
        # 取前几行作为摘要
        content_preview = content[:200].replace('\n', ' ')
        summary_lines.append(f"[{i}] {heading} (行 {start_line}-{end_line}): {content_preview}...")

    summary_text = '\n'.join(summary_lines)

    # 让 LLM 分类
    for attempt in range(1, max_retries + 1):
        try:
            result = ask_ai(
                prompt=f"以下是书籍《{book_name}》按一级标题切分后的各章节摘要。\n\n"
                       f"章节列表：\n{summary_text}\n\n"
                       f"请对每个章节进行分类，并从答案区章节中提取题号→章节的映射关系。",
                system=SystemPrompts.CHAPTER_CLASSIFY.value,
            )

            chapter_map = _parse_llm_json(result)
            if not chapter_map:
                if attempt < max_retries:
                    print(f"[章节拆分] LLM 未返回有效 JSON，第 {attempt}/{max_retries} 次重试")
                    continue
                print("[章节拆分] LLM 重试耗尽，无法获取章节分类")
                return []

            # 保存映射
            map_file = output_dir / "chapter_map.json"
            with open(map_file, 'w', encoding='utf-8') as f:
                json.dump(chapter_map, f, ensure_ascii=False, indent=2)

            # 统计
            content_count = sum(1 for s in chapter_map if s.get('type') == '正文')
            answer_count = sum(1 for s in chapter_map if s.get('type') == '答案区')
            other_count = sum(1 for s in chapter_map if s.get('type') == '其他')
            print(f"[阶段 1] 分类完成：{content_count} 正文 / {answer_count} 答案区 / {other_count} 其他")
            print(f"  映射文件：{map_file}")
            return chapter_map

        except Exception as e:
            if attempt < max_retries:
                print(f"[章节拆分] 第 {attempt}/{max_retries} 次失败：{e}，重试")
                continue
            print(f"[章节拆分] 重试耗尽：{e}")
            return []


def stage2_merge(input_file: str, chapter_map: list[dict],
                 output_dir: str = None) -> Path:
    """
    阶段 2：按映射合并章节+答案，输出每章独立 md 文件

    Args:
        input_file: 整书 md 文件路径
        chapter_map: 阶段 1 产出的章节分类映射
        output_dir: 输出目录

    Returns:
        输出目录路径
    """
    input_path = Path(input_file)
    if output_dir is None:
        output_dir = input_path.parent / "chapter_splited"
    else:
        output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    with open(input_path, 'r', encoding='utf-8') as f:
        md_content = f.read()

    sections = _build_sections_with_lines(md_content)

    # 按类型分组
    content_sections: dict[str, tuple[str, str]] = {}  # chapter_id -> (heading, content)
    answer_sections: list[tuple[str, str, dict]] = []  # (heading, content, chapter_map)

    for i, (heading, content, start_line, end_line) in enumerate(sections):
        # 查找映射中对应的条目
        map_entry = None
        for entry in chapter_map:
            if entry.get('heading', '').strip() == heading.strip():
                map_entry = entry
                break

        if map_entry is None:
            # 映射中找不到的章节，默认当作"其他"
            ch_id = sanitize_filename(heading)[:30]
            content_sections[ch_id] = (heading, content)
            continue

        entry_type = map_entry.get('type', '其他')
        ch_id = map_entry.get('chapter_id', sanitize_filename(heading)[:30])

        if entry_type == '正文':
            content_sections[ch_id] = (heading, content)
        elif entry_type == '答案区':
            answer_sections.append((heading, content, map_entry.get('chapter_map', {})))
        else:
            content_sections[ch_id] = (heading, content)

    # 从答案区提取各章节的答案块
    answer_blocks: dict[str, list[str]] = {}
    for heading, content, ch_map in answer_sections:
        blocks = _extract_answer_blocks(content, ch_map)
        for ch_id, block_list in blocks.items():
            answer_blocks.setdefault(ch_id, []).extend(block_list)

    # 合并并输出
    book_name = sanitize_filename(input_path.stem)
    output_count = 0

    for ch_id, (heading, content) in content_sections.items():
        output_count += 1
        safe_name = sanitize_filename(heading)
        if len(safe_name) > 60:
            safe_name = safe_name[:60]
        output_file = output_dir / f"{output_count:03d}@{book_name}@{ch_id}@{safe_name}.md"

        # 组合正文 + 答案
        parts = [f"{heading}\n\n{content}"]
        if ch_id in answer_blocks:
            parts.append("\n\n---\n\n## 答案与提示\n\n" + '\n\n'.join(answer_blocks[ch_id]))

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(parts))

        has_answer = ch_id in answer_blocks
        print(f"  [{output_count:03d}] {heading[:50]} -> {output_file.name}"
              f" {'(含答案)' if has_answer else '(无答案)'}")

    print(f"[阶段 2] 合并完成，输出 {output_count} 个章节文件")
    print(f"  输出目录：{output_dir}")
    return output_dir


def run_chapter_split_pipeline(input_file: str, output_dir: str = None,
                                max_retries: int = 3) -> Path:
    """
    运行章节拆分 Pipeline：分类 → 合并

    Args:
        input_file: 整书 md 文件路径或目录
        output_dir: 输出目录
        max_retries: LLM 调用重试次数

    Returns:
        输出目录路径
    """
    input_path = Path(input_file)

    print("=" * 60)
    print("章节拆分 Pipeline")
    print("=" * 60)
    print(f"输入：{input_file} ({'目录' if input_path.is_dir() else '文件'})")
    print("=" * 60 + "\n")

    if input_path.is_dir():
        md_files = list(input_path.glob("*.md"))
        if not md_files:
            print("输入目录中未找到 .md 文件")
            return None

        final_dir = None
        for md_file in sorted(md_files):
            print(f"\n处理：{md_file.name}")
            chapter_map = stage1_classify(str(md_file), output_dir, max_retries)
            if not chapter_map:
                print(f"  {md_file.name} 分类失败，跳过")
                continue
            final_dir = stage2_merge(str(md_file), chapter_map, output_dir)

        return final_dir

    # 单文件
    chapter_map = stage1_classify(input_file, output_dir, max_retries)
    if not chapter_map:
        raise RuntimeError("阶段 1 失败")

    return stage2_merge(input_file, chapter_map, output_dir)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="章节拆分 Pipeline")
    parser.add_argument("input_file", nargs="?", default="book",
                        help="输入文件路径或目录")
    parser.add_argument("-o", "--output-dir", type=str, help="输出目录")
    parser.add_argument("-r", "--retries", type=int, default=3,
                        help="LLM 调用重试次数")

    args = parser.parse_args()

    run_chapter_split_pipeline(
        input_file=args.input_file,
        output_dir=args.output_dir,
        max_retries=args.retries,
    )