#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用 Python 生成类似于下图中的字母验证码图片
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string
import os
import errno

target_dir = 'captcha'


def random_letter():
    letter = random.choice(string.ascii_uppercase)
    # print(letter)
    return letter


def random_color():
    color = (random.randint(0, 255),
             random.randint(0, 255), random.randint(0, 255))
    return color


def generate_captcha(num):
    # If to generate more than one captcha, then put in sub-dir: captcha/*.jpg
    # Else put in same dir, named captcha.jpg
    if num > 1:
        # Check for target directory
        try:
            os.makedirs(target_dir)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise

    for img_num in range(num):
        # Generate canvas for captcha
        canvas_width = 240
        canvas_height = 60
        canvas = Image.new('RGB', (canvas_width, canvas_height), '#fff')

        font = ImageFont.truetype('Arial.ttf', 45)
        draw = ImageDraw.Draw(canvas)

        # Generate random 4 digit captcha with random color
        for i in range(4):
            text_pox = 60 * i + random.randint(5, 15)
            text_poy = random.randint(2, 10)
            draw.text((text_pox, text_poy), random_letter(),
                      fill=random_color(), font=font)

        # Generate noise in canvas background
        for _ in range(random.randint(1500, 3000)):
            draw.point((random.randint(0, canvas_width),
                        random.randint(0, canvas_height)), fill=random_color())

        # Blur the text
        canvas = canvas.filter(ImageFilter.BLUR)
        if num > 1:
            canvas.save(target_dir + '/' + str(img_num) + '.jpg', 'jpeg')
        else:
            canvas.save(target_dir + '.jpg', 'jpeg')


def main():
    generate_captcha(1)


if __name__ == '__main__':
    main()
