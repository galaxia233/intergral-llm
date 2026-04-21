"""
格式化 Pipeline

将拆分产出的题目 md 文件转换为 JSON 数组
每个 md 文件交给 LLM，由 LLM 判断题目/答案/解答的位置并输出完整 JSON 对象
根据 has_ref 字段分文件输出：question.json 和 question_ref.json
增量写入：每处理完一个 md 文件就更新 JSON 文件，支持断点续跑
"""

import json
import os
import re
import sys
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from api_client import ask_ai
from system_prompts import SystemPrompts


def extract_source_id_from_filename(filename: str) -> tuple[str, str]:
    """从文件名提取 source 和 id
    source = 第一个下划线之前的部分
    id = 第一个下划线之后的部分
    例：051_2238_2.md → source="051", id="2238_2"
    """
    stem = Path(filename).stem
    idx = stem.find('_')
    if idx == -1:
        return stem, stem
    return stem[:idx], stem[idx + 1:]


def parse_llm_json(result: str) -> list[dict]:
    """从 LLM 返回中提取 JSON，支持单个对象或数组"""
    problems = []

    # 先尝试提取 JSON 数组（多个题目）
    for json_match in re.finditer(r'\[[\s\S]*?\](?:\s*$)', result):
        try:
            data = json.loads(json_match.group())
            if isinstance(data, list):
                for item in data:
                    if isinstance(item, dict) and item.get('question'):
                        problems.append(item)
                if problems:
                    return problems
        except json.JSONDecodeError:
            continue

    # 再尝试提取单个 JSON 对象
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
                    if isinstance(data, dict) and data.get('question'):
                        problems.append(data)
                        return problems
                except json.JSONDecodeError:
                    break

    return problems


file_lock = threading.Lock()
success_counter = {"count": 0}
fail_counter = {"count": 0}


def load_json_array(filepath: Path) -> list[dict]:
    """读取 JSON 数组文件，不存在则返回空列表"""
    if not filepath.exists():
        return []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def save_json_array(filepath: Path, items: list[dict]):
    """写入 JSON 数组文件"""
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)


def append_to_json_array(filepath: Path, new_items: list[dict]):
    """增量追加：读取已有 JSON 数组，追加新项，写回文件"""
    with file_lock:
        existing = load_json_array(filepath)
        existing.extend(new_items)
        save_json_array(filepath, existing)


def load_processed_set(question_file: Path, question_ref_file: Path) -> set[str]:
    """从已有 JSON 文件中提取已处理的文件名（source_id 组合，即 source+"_"+id）"""
    processed = set()
    for json_file in [question_file, question_ref_file]:
        items = load_json_array(json_file)
        for item in items:
            source = item.get('source', '')
            id_str = item.get('id', '')
            if source and id_str:
                processed.add(f"{source}_{id_str}")
    return processed


def process_md_file(file_path: Path, question_file: Path, question_ref_file: Path,
                    max_retries: int = 2) -> list[dict]:
    """处理单个 md 文件：交给 LLM 判断题目/答案/解答 + tag + has_ref，失败时重试"""
    source, id_str = extract_source_id_from_filename(file_path.name)

    print(f"Processing: {file_path.name}")
    for attempt in range(1, max_retries + 1):
        try:
            result = ask_ai(
                prompt="请从文件内容中识别题目、答案、解答，并判断分类标签和是否引用其他题目，输出 JSON。",
                files=str(file_path),
                system=SystemPrompts.MD_TO_JSON.value
            )

            problems = parse_llm_json(result)
            if not problems:
                if attempt < max_retries:
                    print(f"  [{file_path.name}] 未识别到题目，第 {attempt}/{max_retries} 次重试")
                    continue
                print(f"  [{file_path.name}] 未识别到题目，重试 {max_retries} 次后跳过")
                with file_lock:
                    fail_counter["count"] += 1
                return []

            # 强制覆盖 source 和 id（从文件名直接提取，不依赖 LLM 输出）
            for i, problem in enumerate(problems):
                problem['source'] = source
                if len(problems) == 1:
                    problem['id'] = id_str
                else:
                    problem['id'] = f"{id_str}_{i+1}"

            # 根据 reference 分到不同文件
            ref_problems = [p for p in problems if p.get('reference')]
            normal_problems = [p for p in problems if not p.get('reference')]

            if normal_problems:
                append_to_json_array(question_file, normal_problems)
            if ref_problems:
                append_to_json_array(question_ref_file, ref_problems)

            with file_lock:
                success_counter["count"] += len(problems)

            ref_count = len(ref_problems)
            print(f"  [{file_path.name}] 提取 {len(problems)} 道题目 (引用: {ref_count}, 题号: {[p.get('reference', []) for p in ref_problems]})")
            return problems

        except Exception as e:
            if attempt < max_retries:
                print(f"  [{file_path.name}] 第 {attempt}/{max_retries} 次失败：{e}，重试")
                continue
            print(f"  [{file_path.name}] 重试 {max_retries} 次后失败：{e}")
            with file_lock:
                fail_counter["count"] += 1
            return []


def run_format_pipeline(input_dir: str, output_dir: str = None,
                        max_workers: int = 8, resume: bool = True) -> Path:
    """
    运行格式化 Pipeline

    Args:
        input_dir: 拆分产出的题目 md 文件目录
        output_dir: 输出目录（可选），question.json 和 question_ref.json 会放在这里
        max_workers: 并发数
        resume: 是否断点续跑（跳过已处理的文件）

    Returns:
        输出目录路径
    """
    global success_counter, fail_counter
    success_counter = {"count": 0}
    fail_counter = {"count": 0}

    input_path = Path(input_dir)

    if output_dir is None:
        output_dir = input_path.parent / "formatted"
    else:
        output_dir = Path(output_dir)

    output_dir.mkdir(parents=True, exist_ok=True)

    question_file = output_dir / "question.json"
    question_ref_file = output_dir / "question_ref.json"

    md_files = list(input_path.glob("*.md"))

    # 断点续跑：跳过已处理的文件（按 source_id 组合匹配）
    if resume:
        processed = load_processed_set(question_file, question_ref_file)
        md_files = [f for f in md_files if f.stem not in processed]
        if processed:
            print(f"[格式化] 断点续跑：跳过 {len(processed)} 个已处理文件")

    print(f"[格式化] 待处理 {len(md_files)} 个题目文件")
    print(f"  并发数：{max_workers}\n")

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(process_md_file, f, question_file, question_ref_file): f for f in md_files}
        for future in as_completed(futures):
            future.result()

    # 统计最终结果
    q_count = len(load_json_array(question_file))
    qr_count = len(load_json_array(question_ref_file))

    print(f"\n[格式化] 完成！")
    print(f"  成功：{success_counter['count']} | 失败：{fail_counter['count']}")
    print(f"  question.json: {q_count} 道题")
    print(f"  question_ref.json: {qr_count} 道题（含引用）")
    print(f"  输出目录：{output_dir}")
    return output_dir


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="题目格式化 Pipeline")
    parser.add_argument("input_dir", help="题目 md 文件目录")
    parser.add_argument("-o", "--output-dir", type=str, help="输出目录")
    parser.add_argument("-w", "--workers", type=int, default=8,
                        help="并发数")
    parser.add_argument("--no-resume", action="store_true",
                        help="不使用断点续跑，从头开始")

    args = parser.parse_args()

    run_format_pipeline(
        input_dir=args.input_dir,
        output_dir=args.output_dir,
        max_workers=args.workers,
        resume=not args.no_resume,
    )