#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
"""

import re

file = 'filtered_words.txt'


def filter_input(word):
    filter_word = open(file, 'r', encoding='utf-8').read()
    if word == '' or len(re.findall(r'%s' % (word), filter_word)) == 0:
        print('Human Rights')
    else:
        print('Freedom')
    # print('Filter done.')


def main():
    user_input = input("Your input here:")
    filter_input(user_input)


if __name__ == '__main__':
    main()
