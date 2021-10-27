#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu
Date   : 2021-10-26
Purpose: Find common words
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Find common words",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "FILE1", metavar="FILE", help="Input file 1", type=argparse.FileType("rt")
    )

    parser.add_argument(
        "FILE2", metavar="FILE", help="Input file 2", type=argparse.FileType("rt")
    )

    parser.add_argument(
        "-k", "--kmer", metavar="Str", type=int, default="3", help="K-mer size"
    )

    args = parser.parse_args()

    if args.kmer < 1:
        parser.error(f'--kmer "{args.kmer}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    words1 = {}
    for line in args.FILE1:
        for words in line.split():
            for kmer in find_kmers(words, args.kmer):
                if kmer in words1:
                    words1[kmer] += 1
                else:
                    words1[kmer] = 1

    words2 = {}
    for line in args.FILE2:
        for words in line.split():
            for kmer in find_kmers(words, args.kmer):
                if kmer in words2:
                    words2[kmer] += 1
                else:
                    words2[kmer] = 1

    for kmer in words1:
        if kmer in words2:
            print(f"{kmer:10}{words1.get(kmer):6}{words2.get(kmer):6}")


# --------------------------------------------------
def find_kmers(seq, k):
    """Find k-mers in string"""

    n = len(seq) - k + 1
    return [] if n < 1 else [seq[i : i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers():
    """Test find_kmers"""

    assert find_kmers("", 1) == []
    assert find_kmers("ACTG", 1) == ["A", "C", "T", "G"]
    assert find_kmers("ACTG", 2) == ["AC", "CT", "TG"]
    assert find_kmers("ACTG", 3) == ["ACT", "CTG"]
    assert find_kmers("ACTG", 4) == ["ACTG"]
    assert find_kmers("ACTG", 5) == []


# --------------------------------------------------
if __name__ == "__main__":
    main()
