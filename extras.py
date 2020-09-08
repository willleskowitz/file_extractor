#!/usr/bin/env python
"""
# Name:         Will Leskowitz
# Project:      File Extractor
# Script:       get_extensions
# Date:         Thu Sep  3 19:19:57 2020
#
"""

def compile_extensions(extensions):
    categories = {'common_media': ('.jpg', '.jpeg', '.mp4', '.mov', '.wmv',
                                   '.avi'),

                  'images': ('.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi',
                             '.png', '.gif', '.webp', '.tiff', '.tif', '.jp2',
                             '.raw', '.arw', '.cr2', '.nrw', '.k25', '.bmp',
                             '.dib', '.heif', '.heic', '.j2k', '.jpf', '.jpx',
                             '.jpm', '.mj2'),

                  'vector': ('.svg', '.svgz', '.ai', '.eps', '.pdf'),

                  'videos': ('.mp4', '.mov', '.wmv', '.avi', '.qt', '.mkv',
                             '.avchd', '.flv', '.swf', '.h264', '.h265',
                             '.mpeg4', '.dixv', '.xvid', '.mj2',),

                  'audio': ('mp3', '.pcm', '.wav', '.aiff', '.aif', '.aifc',
                            '.aac', '.m4a', '.mp4', '.wma', '.flac', '.snd'),

                  'documents': ('.pdf', '.xls', '.doc', '.xlsx', '.docx',
                                '.pptx', '.csv')}

    # Convert to list
    extensions = list(extensions)

    # Ensure extensions are correctly formatted
    for i, extension in enumerate(extensions):
        new_ext = extension.lower()

        if new_ext[0] != '.' and new_ext not in categories:
            new_ext = '.' + new_ext

        extensions[i] = new_ext

    # Convert to set to avoid duplicates
    extensions = set(extensions)

    # Compile extensions of interested files
    for category in categories:
        if category in extensions:
            extensions.remove(category)
            extensions.update(categories[category])

    return extensions


def progress_bar(iteration, total):
    prefix = 'Progress:'
    suffix = 'Complete'
    complete_message = 'Operation Completed'
    decimals = 1
    length = 50
    fill = '>'

    percent = str(round(100 * iteration / total, decimals))
    filled_len = int(length * iteration // total)
    bar = fill * filled_len + '-' * (length - filled_len)
    print_line = '\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix)
    print(print_line, end = '\r')

    if iteration == total:
        side_len = (len(print_line) - len(complete_message)) // 2 - 1
        print('>' * side_len, complete_message, '<' * side_len)
