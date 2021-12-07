#!/usr/bin/env python3
"""
Author : shv <shv@localhost>
Date   : 2021-12-02
Purpose: a cat in reverse
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python clone of tac",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "files",
        metavar="FILE",
        help="Input file(s)",
        type=argparse.FileType("rt"),
        nargs="+",
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
    """soda pop"""

    args = get_args()
    for fh in args.files:
        for line in reversed(fh.readlines()):
            print(line, end="", file=args.outfile)


# --------------------------------------------------
if __name__ == "__main__":
    main()
