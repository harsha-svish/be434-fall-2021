#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu>
Date   : 2021-09-28
Purpose: to conCATenate files
"""

import argparse


# --------------------------------------------------


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="To concatenate files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
	help=("A readable file"),
	metavar="FILE",
	nargs="+",
	type=(argparse.FileType("rt"))
	)

    parser.add_argument(
        "-n", "--number", help="Number the lines", action="store_true", default="FALSE"
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        # for i, line in enumerate(args.file, start=1):
        for i, line in enumerate(fh, start=1):
            if args.number is True:
                print("     {}	{}".format(i, line), end="")
            else:
                print(line, end="")


# --------------------------------------------------
if __name__ == "__main__":
    main()
