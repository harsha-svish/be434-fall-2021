#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu>
Date   : 2021-10-05
Purpose: Translate DNA/RNA to AA
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Python program to translate DNA/RNA to AA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument("sequence", metavar="str", help="DNA/RNA sequence")

    parser.add_argument(
        "-c",
        "--codons",
        help="A file with codon translations",
        metavar="FILE",
        required=True,
        type=argparse.FileType("rt"),
        default=None,
    )

    parser.add_argument(
        "-o",
        "--outfile",
        help="Output filename",
        metavar="FILE",
        type=argparse.FileType("wt"),
        default="out.txt",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    seq = args.sequence.upper()
    ama = args.outfile
    codon_table = {}  # initialize codon_table to empty dictionary

    for line in args.codons:
        codon, aa = line.split()
        codon_table[codon] = aa

    k = 3
    for codon in [seq[i:i + k] for i in range(0, len(seq), k)]:
        ama.write(codon_table.get(codon.upper(), "-"))  # method within method
    print('Output written to "{}".'.format(ama.name))


# --------------------------------------------------
if __name__ == "__main__":
    main()
