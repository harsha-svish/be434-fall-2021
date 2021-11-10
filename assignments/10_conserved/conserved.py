#!/usr/bin/env python3
"""
Author : shv <shv@localhost>
Date   : 2021-11-10
Purpose: Find conserved bases
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Rock the Casbah",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE",
        help="Input file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.FILE.read().split()
    # print(seq)
    print("\n".join(seq))
    for i in range(len(seq[0])):
        bases = []
        for num in seq:
            bases += num[i]
        common = all(x == bases[0] for x in bases)
        if common:
            print("|", end="")
        else:
            print("X", end="")
    print()


# --------------------------------------------------
if __name__ == "__main__":
    main()
