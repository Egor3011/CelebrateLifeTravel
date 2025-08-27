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



def addNewUser(name: str, tel: str, tour: str):
    try:
        cursor, connection = mysqlDB()
        cursor.execute(f"INSERT INTO users (name, tel, tour) VALUES ('{name}', '{tel}', '{tour}');")
        return connection.commit()
    except Exception as ex:
        return ex


def getUserInfo(id: int):
    try:
        cursor, connection = mysqlDB()
        cursor.execute(f"SELECT name, tel, tour FROM `users` WHERE id = {id}")
        userInfo = cursor.fetchall()
        return userInfo
    except Exception as ex:
        return ex