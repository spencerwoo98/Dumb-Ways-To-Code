"""
将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
"""

import pymysql
import uuid


def generate_promo_code(count):
    promoCode = []

    for i in range(count):
        code = str(uuid.uuid4()).replace('-', '').upper()
        # print(code)
        promoCode.append(code)

    print('---> Generated ' + str(count) + ' promotion codes.')
    return promoCode


def upload_to_sql(promoCode):
    print('---> Connecting to Database...')
    try:
        dbHost = 'localhost'
        dbUser = 'root'
        dbPwd = 'Genius98!'
        promoCodeDB = pymysql.connect(
            host=dbHost, user=dbUser, password=dbPwd, db='mysql')
        dbCursor = promoCodeDB.cursor()
        print('---> Connected!')

    except BaseException as e:
        print(e)

    else:
        try:
            print('---> Trying to upload data into database...')
            dbCursor.execute('CREATE DATABASE IF NOT EXISTS `promo_code_db`')
            dbCursor.execute('USE `promo_code_db`')
            dbCursor.execute(
                '''CREATE TABLE IF NOT EXISTS `promo_code`(
                    `code_id` INT NOT NULL AUTO_INCREMENT, 
                    `code_key` VARCHAR(32) NOT NULL, 
                    PRIMARY KEY(`code_id`));
                    ''')

            for eachCode in promoCode:
                dbCursor.execute(
                    'INSERT INTO promo_code(code_key) VALUES(%s);', (eachCode))
                dbCursor.connection.commit()

            print('---> Upload data success!')

        except BaseException as e:
            print('---> Upload data failed!')
            print(e)

    finally:
        dbCursor.close()
        promoCodeDB.close()


def main():
    upload_to_sql(generate_promo_code(200))


if __name__ == '__main__':
    main()
