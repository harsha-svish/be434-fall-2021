#!/usr/bin/env python3
"""
Author : shv <shv@localhost>
Date   : 2021-11-23
Purpose: Rock the Casbah
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("pattern", metavar="PATTERN", help="Search pattern")

    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="+",
        help="Input file(s)",
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "-i", "--insensitive", help="case-insensitive search", action="store_true"
    )
    parser.add_argument(
        "-o",
        "--outfile",
        help="Output file",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for fh in args.files:
        for line in fh:
            case1 = re.search(args.pattern, line, re.I)
            case2 = re.search(args.pattern, line)
            if args.insensitive:
                if (case1) and (len(args.files) > 1):
                    print(f"{fh.name}:{line}", file=args.outfile, end="")
                if (case1) and (len(args.files) == 1):
                    print(line, file=args.outfile, end="")
            else:
                if (case2) and (len(args.files) > 1):
                    print(f"{fh.name}:{line}", file=args.outfile, end="")
                if (case2) and (len(args.files) == 1):
                    print(line, file=args.outfile, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
