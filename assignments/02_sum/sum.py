#!/usr/bin/env python3
"""
Author : shv <shv@localhost>
Date   : 2021-09-14
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('num',
                        metavar='int',
                        nargs='+',
                        help='Numbers to add',
                        type=int)

    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    num = args.num
    count = len(num)

    add = 0
    mun = ''
    summation = ''
    if count == 1:
        summation = num [0]
        add = num [0]
        print(f'{summation} = {add}')
    else:
        add = sum(num)
        mun = [str(n) for n in num]
        summation = ' + '.join(mun)
        print(f'{summation} = {add}')
        
# --------------------------------------------------
if __name__ == '__main__':
    main()
