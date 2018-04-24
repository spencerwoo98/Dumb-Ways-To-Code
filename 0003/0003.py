#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 Redis 非关系型数据库中。
"""

import uuid
import redis


def generate_promo_code(count):
    promoCode = []

    for i in range(count):
        code = str(uuid.uuid4()).replace('-', '').upper()
        # print(code)
        promoCode.append(code)

    print('---> Generated ' + str(count) + ' promotion codes.')
    return promoCode


def upload_to_redis(promoCode):
    myHost = 'localhost'
    myPort = 6379

    try:
        print('---> Trying to connect to redis...')
        r = redis.StrictRedis(host=myHost, port=myPort, decode_responses=True)
        r.flushdb()
        for eachCode, key in zip(promoCode, range(1, len(promoCode)+1)):
            # print(str(key) + ': ' + eachCode)
            r.set(key, eachCode)
        print('---> Upload success!')

    except BaseException as e:
        print(e)


def main():
    upload_to_redis(generate_promo_code(200))


if __name__ == '__main__':
    main()
