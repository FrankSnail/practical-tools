import os
import argparse
from fstools import list_large_files


units = {
    'B': 1,
    'K': 1024,
}
units['M'] = units['K'] * 1024
units['G'] = units['M'] * 1024
units['T'] = units['G'] * 1024




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('path', default='.')
    parser.add_argument('-no-recursive', action='store_true')
    parser.add_argument('-size', default="1M")

    args = parser.parse_args()
    unit = 'B'
    if args.size[-1].isalpha():
        unit = args.size[-1].upper()
        args.size = args.size[:-1]
    if unit not in set(['B', 'K', 'M', 'G', 'T']):
        print("Invalid file size unit[{}]".format(unit))
        exit(1)
    if not args.size.isnumeric():
        print("Invalid file size [{}]".format(args.size))
        exit(1)
    size = float(args.size)
    size *= units[unit]
    recursive = True
    if args.no_recursive:
        recursive = False
    list_large_files(args.path, size, recursive)
