#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
"""

import os
from PIL import Image
import glob


origin_dir = 'original'
target_dir = 'result'
# threshold: iPhone 5 maximum resolution
width_limit = 1136
height_limit = 640


def compress_image(image_dir, result_dir, target_width, target_height):
    working_dir = os.path.dirname(os.path.realpath(__file__))

    try:
        print('---> Loading images...')
        my_images = glob.glob('{}/*'.format(image_dir))
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        for each_img, i in zip(my_images, range(1, len(my_images)+1)):
            print(str(i) + ':', each_img)
            with Image.open(each_img) as img:
                width, height = img.size
                # print(each_img, width, height, os.path.getsize(each_img))
                if os.path.getsize(each_img) > target_width * target_height:
                    # print(each_img)
                    if width > height:
                        new_width = target_width
                        new_height = int(new_width * height / width)
                    else:
                        new_height = target_width
                        new_width = int(new_height * width / height)
                    # print(new_width, new_height)
                    result_img = img.resize((new_width, new_height))
                    result_img_name = each_img.replace(image_dir, result_dir)
                    result_img.save(result_img_name)

        print('--->', i, 'images loaded and compressed.')
        print('---> Saved in', working_dir + '/' + result_dir)

    except OSError as e:
        print(e)


def main():
    compress_image(origin_dir, target_dir, width_limit, height_limit)


if __name__ == '__main__':
    main()
