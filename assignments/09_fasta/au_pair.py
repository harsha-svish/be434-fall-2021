#!/usr/bin/env python3
"""
Author : shv <shv@localhost>
Date   : 2021-11-02
Purpose: Split paired reads
"""

import argparse
import os
from Bio import SeqIO


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Split paired reads",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="input file",
        metavar="FILE",
        nargs="+",
        type=argparse.FileType("rt"),
    )

    parser.add_argument(
        "-o",
        "--outdir",
        type=str,
        metavar="DIR",
        help="Output directory",
        default="split",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_dir = args.outdir

    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)

    for fh in args.file:
        copyname = os.path.basename(fh.name)
        root, ext = os.path.splitext(copyname)

        reader = SeqIO.parse(fh.name, "fasta")
        seq_odd = []
        seq_even = []
        i = 1
        for rec in reader:
            if i % 2 == 0:
                seq_even.append(rec)
            else:
                seq_odd.append(rec)
            i += 1

        SeqIO.write(seq_even, os.path.join(args.outdir, root + "_1" + ext), "fasta")
        SeqIO.write(seq_odd, os.path.join(args.outdir, root + "_2" + ext), "fasta")

    print('Done, see output in "{}"'.format(args.outdir))


# --------------------------------------------------
if __name__ == "__main__":
    main()
