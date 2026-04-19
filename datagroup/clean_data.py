import json
from typing import Any, Dict, List

PROOF_KEYWORDS = ['证明', 'prove', 'show that', 'verify that']


def _has_empty_field(obj: Any, parent_key: str = '') -> bool:
    """递归检查对象是否包含空字段（空字符串、None、空列表），但 tag.tools_solvable 允许为空列表"""
    if isinstance(obj, dict):
        for k, v in obj.items():
            if _has_empty_field(v, parent_key=k):
                return True
        return False
    if isinstance(obj, list):
        if parent_key == 'tools_solvable':
            return False
        return len(obj) == 0
    if obj is None:
        return True
    if isinstance(obj, str) and not obj.strip():
        return True
    return False


def clean_json_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    清洗 JSON 数据：删除证明题，删除任意字段为空的记录。

    Args:
        data: JSON 数组

    Returns:
        清洗后的 JSON 数组
    """
    proof_removed = 0
    empty_removed = 0
    duplicate_removed = 0

    seen_questions = set()
    cleaned = []
    for i, item in enumerate(data):
        question = item.get('question', '')

        if any(kw.lower() in question.lower() for kw in PROOF_KEYWORDS):
            proof_removed += 1
            continue

        if _has_empty_field(item):
            empty_removed += 1
            continue

        if question in seen_questions:
            duplicate_removed += 1
            continue
        seen_questions.add(question)

        cleaned.append(item)

    print(f"原始: {len(data)} | 清洗后: {len(cleaned)} | 删除: {len(data) - len(cleaned)}")
    print(f"  证明题删除: {proof_removed}")
    print(f"  空字段删除: {empty_removed}")
    print(f"  重复题删除: {duplicate_removed}")
    print(f"  保留率: {len(cleaned)/len(data)*100:.1f}%")

    return cleaned


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        file_path = '../database/积分题目示例数据.json'

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    result = clean_json_data(data)

    out_path = file_path.replace('.json', '_cleaned.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"已保存至: {out_path}")