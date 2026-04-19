"""
题目处理 Pipeline 入口

拆分流水线（切分 + LLM提取）在 split/pipeline.py 中
后续格式化流水线待开发
"""

from split.pipeline import run_split_pipeline

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="题目处理 Pipeline")
    parser.add_argument("input_file", nargs="?", default="books",
                        help="输入文件路径或目录")
    parser.add_argument("-1", "--stage1-output", type=str, help="切分输出目录")
    parser.add_argument("-2", "--stage2-output", type=str, help="题目提取输出目录")
    parser.add_argument("-w", "--workers", type=int, default=4,
                        help="LLM 提取并发数")

    args = parser.parse_args()

    run_split_pipeline(
        input_file=args.input_file,
        stage1_output=args.stage1_output,
        stage2_output=args.stage2_output,
        max_workers=args.workers,
    )