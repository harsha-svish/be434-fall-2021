#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu>
Date   : 2021-10-17
Purpose: DNA IUPAC codes to regular expression
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="DNA IUPAC Codes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("SEQ", nargs="+", help="Input sequence(s)")

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default=sys.stdout,
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    code = {
        "A": "A",
        "C": "C",
        "G": "G",
        "T": "T",
        "U": "U",
        "R": "[AG]",
        "Y": "[CT]",
        "S": "[GC]",
        "W": "[AT]",
        "K": "[GT]",
        "M": "[AC]",
        "B": "[CGT]",
        "D": "[AGT]",
        "H": "[ACT]",
        "V": "[ACG]",
        "N": "[ACGT]",
    }

    for seq in args.SEQ:
        line = seq + " "
        for char in seq:
            line += char if char in "ACGTU" else code.get(char, "-")
        print(line, file=args.outfile)

    if args.outfile is not sys.stdout:
        print(f'Done, see output in "{args.outfile.name}"')


# --------------------------------------------------
if __name__ == "__main__":
    main()
