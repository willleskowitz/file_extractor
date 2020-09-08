#!/usr/bin/env python
"""Command line interface for extracting files from directories."""

import argparse
import transfer_files

def main():
    parser = argparse.ArgumentParser(description='File Extractor')
    parser.add_argument('action')

    args = parser.parse_args()
    if args.action == 'copy':
        transfer_files.copy_files()

    elif args.action == 'move':
        transfer_files.move_files()

    else:
        print('error: Invalid action provided.')

if __name__ == '__main__':
    main()