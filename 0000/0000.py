from PIL import Image, ImageDraw, ImageFont


def add_unread_count(img):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    textSize = int(width*0.15)
    textColor = '#CB1B45'
    textFont = ImageFont.truetype('Arial.ttf', textSize)
    draw.text((width*0.8, height*0.02), '99', font=textFont, fill=textColor)
    img.save('icon_added.jpg', 'jpeg')


def main():
    img = Image.open('icon.jpg')
    add_unread_count(img)


if __name__ == '__main__':
    main()
