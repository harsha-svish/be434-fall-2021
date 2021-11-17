#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu>
Date   : 2021-11-16
Purpose: Run length encoding
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("str", metavar="str", help="DNA text or file")

    args = parser.parse_args()

    if os.path.isfile(args.str):
        args.str = open(args.str).read()

    return args


# --------------------------------------------------
def main():
    """Zoom"""

    args = get_args()
    for seq in args.str.splitlines():
        print(rle(seq))


# --------------------------------------------------
def rle(seq):
    "creating RLE"

    encoded_dna = ""
    i = 0

    while i <= len(seq) - 1:
        count = 1
        ch = seq[i]
        j = i
        while j < len(seq) - 1:
            if seq[j] == seq[j + 1]:
                count = count + 1
                j = j + 1
            else:
                break
        encoded_dna = encoded_dna + ch + str(count)
        i = j + 1
    return encoded_dna


# -------------------------------------------------------
def test_rle():
    """Test rle"""

    assert rle("A") == "A"
    assert rle("ACGT") == "ACGT"
    assert rle("AA") == "A2"
    assert rle("AAAAA") == "A5"
    assert rle("ACCGGGTTTT") == "AC2G3T4"


# --------------------------------------------------
if __name__ == "__main__":
    main()
