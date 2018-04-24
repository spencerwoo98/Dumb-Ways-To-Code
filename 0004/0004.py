#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
任一个英文的纯文本文件，统计其中的单词出现的个数。
"""

import re


def word_count(fileName):
    file = open(fileName, 'r')
    content = file.read()
    words = re.findall(r'[a-zA-Z0-9]+', content)
    # print(words)
    return len(words)


def main():
    file = 'demo.txt'
    num = word_count(file)
    print(num)


if __name__ == '__main__':
    main()
