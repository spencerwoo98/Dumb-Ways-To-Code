#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""

import re

file = 'filtered_words.txt'


def filter_input(word):
    filter_word = open(file, 'r', encoding='utf-8').read().splitlines()
    # if word == '' or len(re.findall(r'%s' % (word), filter_word)) == 0:
    for each_word in filter_word:
        if word == '':
            print('Human Rights')
        elif word == each_word:
            print('Human Rights')
        else:
            print('Freedom')
    # print('Filter done.')


def main():
    user_input = input("Your input here:")
    filter_input(user_input)


if __name__ == '__main__':
    main()
