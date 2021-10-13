#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu
Date   : 2021-10-12
Purpose: Find commone words
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('FILE1',
                        metavar='FILE',
                        help='Input file 1',
                        type=argparse.FileType('rt'))

    parser.add_argument('FILE2',
                        metavar='FILE',
                        help='Input file 2',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    book1 = {}
    for line in args.FILE1:
        for word in line.split():
            book1[word] = 1

    book2 = {}
    for line in args.FILE2:
        for word in line.split():
            book2[word] = 1

    for keys in book1:
        if keys in book2:
            print(keys)


# --------------------------------------------------
if __name__ == '__main__':
    main()
