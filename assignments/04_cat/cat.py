#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu>
Date   : 2021-09-28
Purpose: to conCATenate files
"""

import argparse
import os, sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="To concatenate files",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "file",
        help="A readable file",
        metavar="FILE",
        # nargs="+",
        type=argparse.FileType('rt'),
        default=None
    )

    parser.add_argument('-n',
                        '--number',
                        help='Number the lines',
                        action='store_true')

    # args = parser.parse_args()
    
    # if os.path.isfile(args.file):
    #     parser.error(f'"{args.file}" is not a file')
    
    # args.file = open(args.file)
    
    # return args
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for i, line in enumerate(args.file, start=1):
        print(f'{i:6} {line}', end='')

# --------------------------------------------------
if __name__ == "__main__":
    main()
