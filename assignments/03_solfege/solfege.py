#!/usr/bin/env python3
"""
Author : shv <shv@email.arizona.edu>
Date   : 2021-09-21
Purpose: Assignment 3
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Assignment 3',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='str', help='Input text', nargs='+')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    solfege = {
                'Do': 'A deer, a female deer',
                'Re': 'A drop of golden sun',
                'Mi': 'A name I call myself',
                'Fa': 'A long long way to run',
                'Sol': 'A needle pulling thread',
                'La': 'A note to follow sol',
                'Ti': 'A drink with jam and bread'
                }
    for lyr in args.text:
        if lyr in solfege:
            print(f'{lyr}, {solfege.get(lyr, lyr)}')
        else:
            print(f'I don\'t know "{lyr}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
