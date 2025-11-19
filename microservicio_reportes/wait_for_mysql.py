import os
import time
import mysql.connector

host = os.environ["MYSQL_HOST"]
user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
database = os.environ["MYSQL_DATABASE"]

while True:
    try:
        mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("MySQL está listo")
        break
    except mysql.connector.Error:
        print("Esperando MySQL...")
        time.sleep(2)
