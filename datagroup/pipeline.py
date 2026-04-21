"""
题目处理 Pipeline 入口

支持模式：
  split   — 拆分流水线（切分 + LLM提取）
  format  — 格式化流水线（md → JSON）
  all     — 拆分 + 格式化 一起执行
"""

from pathlib import Path
from split.pipeline import run_split_pipeline
from format.pipeline import run_format_pipeline

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="题目处理 Pipeline")
    parser.add_argument("input_file", nargs="?", default="books",
                        help="输入文件路径或目录")
    parser.add_argument("-m", "--mode", choices=["split", "format", "all"], default="all",
                        help="运行模式：split=拆分, format=格式化, all=拆分+格式化")

    # split 参数
    parser.add_argument("-1", "--stage1-output", type=str, help="切分输出目录")
    parser.add_argument("-2", "--stage2-output", type=str, help="题目提取输出目录")
    parser.add_argument("-b", "--batch-start", type=int, default=None,
                        help="批号起始值，不指定时自动检测")
    parser.add_argument("-ws", "--split-workers", type=int, default=4,
                        help="拆分阶段并发数")

    # format 参数
    parser.add_argument("-f", "--format-dir", type=str,
                        help="格式化输入目录（mode=format 时指定题目 md 目录）")
    parser.add_argument("-o", "--format-output", type=str, help="格式化输出目录")
    parser.add_argument("-wf", "--format-workers", type=int, default=8,
                        help="格式化阶段并发数")
    parser.add_argument("--no-resume", action="store_true",
                        help="格式化时不使用断点续跑，从头开始")

    args = parser.parse_args()

    if args.mode == "split":
        run_split_pipeline(
            input_file=args.input_file,
            stage1_output=args.stage1_output,
            stage2_output=args.stage2_output,
            max_workers=args.split_workers,
            batch_start=args.batch_start,
        )

    elif args.mode == "format":
        format_dir = args.format_dir or args.input_file
        run_format_pipeline(
            input_dir=format_dir,
            output_dir=args.format_output,
            max_workers=args.format_workers,
            resume=not args.no_resume,
        )

    elif args.mode == "all":
        split_dir = run_split_pipeline(
            input_file=args.input_file,
            stage1_output=args.stage1_output,
            stage2_output=args.stage2_output,
            max_workers=args.split_workers,
            batch_start=args.batch_start,
        )
        run_format_pipeline(
            input_dir=str(split_dir),
            output_dir=args.format_output,
            max_workers=args.format_workers,
            resume=not args.no_resume,
        )