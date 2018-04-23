""" 
第 0001 题： 
做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券）
使用 Python 如何生成 200 个激活码（或者优惠券）？ 
"""

import uuid


def generate_promo_code(count):
    promoCode = []
    promoCodeFile = open('promo.txt', 'w')

    for i in range(count):
        code = str(uuid.uuid4()).replace('-', '').upper()
        promoCode.append(code)
    for eachCode in promoCode:
        promoCodeFile.write(str(eachCode) + '\n')
    print('Successfully generated ' + str(count) + ' Promo Codes')

    promoCodeFile.close()


def main():
    generate_promo_code(200)


if __name__ == '__main__':
    main()
