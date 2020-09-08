#!/usr/bin/env python
"""
# Name:         Will Leskowitz
# Project:      File Extractor
# Script:       copy_files
# Date:         Thu Sep 3 17:58:11 2020
#
"""

import os
import shutil
import extras

def get_input():
    source_dir = input('Source directory path:\n>>> ')
    final_dir = input('\nFinal directory path:\n>>> ')
    wanted = input('\nExtensions and/or categories of interested files:\n>>> ')

    extensions = extras.compile_extensions(wanted.split())
    print('\nSeleted extensions:\n<<< %s' % ' '.join(sorted(extensions)))

    unwant_str = '''Extensions and/or categories from above you wish to avoid:
>>>'''


    unwanted = input('\n' + unwant_str)
    avoid = extras.compile_extensions(unwanted.split())

    for ext in avoid:
        extensions.discard(ext)

    return source_dir, final_dir, tuple(extensions)


def copy_files():
    copy_dir, paste_dir, extensions = get_input()
    transfer_files(copy_dir, paste_dir, extensions, shutil.copy)


def move_files():
    move_dir, paste_dir, extensions = get_input()
    transfer_files(move_dir, paste_dir, extensions, shutil.move)


def transfer_and_rename(filename, root, basedir, action):
    old_name = os.path.join(os.path.abspath(root), filename)
    base, extension = os.path.splitext(filename)
    new_name = os.path.join(basedir, filename)

    if not os.path.exists(new_name):
        action(old_name, new_name)

    elif os.path.getsize(new_name) != os.path.getsize(old_name):
        ii = 1
        while True:
            new_name = os.path.join(basedir, base + "_" + str(ii) + extension)
            if not os.path.exists(new_name):
                action(old_name, new_name)
                break
            if os.path.getsize(new_name) == os.path.getsize(old_name):
                break
            ii += 1


def transfer_files(source_dir, final_dir, extensions, action):

    if not(extensions):
        print('No extensions selected.')
        return False

    print('\n\rInitializing...', end ='\r')

    # Dir the script will search for intrested files
    source_dir = os.path.normpath(source_dir)

    # Dir the files will be copied into
    final_dir = os.path.normpath(final_dir)

    # Check if paths exist
    if not(os.path.exists(source_dir)) or not(os.path.exists(final_dir)):
        print('\rThere are no files in this directory.')
        return False

    # Find length of directory
    source_len = sum(len(files) for r, d, files in os.walk(source_dir))

    if source_len == 0:
        print('\rThere are no files in this directory.')
        return False

    # initialize progress bar
    i = 0
    extras.progress_bar(i, source_len)

    # Search directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(extensions):
                try:
                    transfer_and_rename(file, root, final_dir, action)

                except PermissionError:
                    pass

            i += 1
            extras.progress_bar(i, source_len)
        # i += len(files)
        # extras.progress_bar(i, source_len)

    return True

if __name__ == '__main__':
    copy_files()