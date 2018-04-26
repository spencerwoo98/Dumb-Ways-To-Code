#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
使用 Python 生成类似于下图中的字母验证码图片
"""

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
import string


def random_letter():
    letter = random.choice(string.ascii_uppercase)
    # print(letter)
    return letter


def random_color():
    color = (random.randint(0, 255),
             random.randint(0, 255), random.randint(0, 255))
    return color


def generate_captcha():
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
    canvas.save('captcha.jpg', 'jpeg')


def main():
    generate_captcha()


if __name__ == '__main__':
    main()
