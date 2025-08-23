import pymysql
import config as cfg

def mysqlDB():
    connection = pymysql.connect(
        host=cfg.mySQL_ADRES,
        port=cfg.mySQL_PORT,
        user=cfg.mySQL_USERNAME,
        password=cfg.mySQL_PASSWORD,
        database=cfg.mySQL_database
    )
    print(f"successfully connected to server...")
    print("-" * 20)
    cursor = connection.cursor()
    return cursor, connection


def getDataCards(cardsSort: str = None):
    a = []
    cursor, connection = mysqlDB()
    insert_query = f"SELECT * FROM `cards`" + cardsSort
    cursor.execute(insert_query)
    connection.commit()
    rows = cursor.fetchall()
    print(rows)
    for row in rows:
        print(row)
        if str(row[6]) != "-":
            a.append({"id": str(row[0]), "title": row[1], "minPrice": row[2], "imgSrc": row[3], "format": row[4]})
    print(a)
    return list(reversed(a))


def getCardInfo(id):
    a = []
    cursor, connection = mysqlDB()
    cursor.execute(f"SELECT id, size, price, format FROM `{id}`")
    connection.commit()
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        a.append({"id": str(row[0]), "size": str(row[1]), "price": str(row[2]), "format": str(row[3])})
    print(a)
    return a


def getPromoInfo(promoStr: str):
    cursor, connection = mysqlDB()
    cursor.execute(f"SELECT percent FROM `promocods` WHERE promo = '{promoStr}'")
    connection.commit()
    percentPromo = cursor.fetchall()[0][0]
    return percentPromo



def createNewTable(name):
    cursor, connection = mysqlDB()
    cursor.execute(f"CREATE TABLE `{name}` (`id` INT NOT NULL AUTO_INCREMENT, `size` VARCHAR(45) NULL, `price` INT NULL, `format` VARCHAR(45) NULL, PRIMARY KEY (`id`));")
    return connection.commit()