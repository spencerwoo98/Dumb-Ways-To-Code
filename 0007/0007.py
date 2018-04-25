#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Designed for c/cpp files

"""
有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""

import re
import glob

target_dir = '/Users/spencerwoo/Documents/Code/C++File'


def count(dir):
    print('---> Opening directory', target_dir)
    files = glob.glob('{}/**/*.c*'.format(dir), recursive=True)
    lines, comments, spaces = (0, 0, 0)

    for each_file in files:
        # print(each_file)
        try:
            code = open(each_file, 'r')

            for line in code.readlines():
                lines += 1
                if line.strip() == '':
                    spaces += 1
                if r'//' in line:
                    comments += 1

        except BaseException as e:
            print(e)

    print(len(files), 'files counted in total.')
    print(lines, 'lines in total.')
    print(comments, 'comments in total.')
    print(spaces, 'white spaces in total.')
    print(lines - comments - spaces, 'lines of raw code in total.')


def main():
    count(target_dir)


if __name__ == '__main__':
    main()
