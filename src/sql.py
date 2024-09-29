import os
import psycopg2

from logger import *

sql = None

def init_sql():
    global sql

    sql_host = os.getenv("DB_HOST")
    sql_port = os.getenv("DB_PORT")
    sql_user = os.getenv("DB_USER")
    sql_password = os.getenv("DB_PASSWORD")
    sql_database = os.getenv("DB_DATABASE")

    sql = psycopg2.connect(dbname=sql_database, user=sql_user, password=sql_password, host=sql_host, port=sql_port)

    log("Initiated sql!")

def sql_do(command):
    cursor = sql.cursor()
    cursor.execute(command)
    sql.commit()
    try:
        reuslt = cursor.fetchall()
        cursor.close()
        return reuslt
    except (psycopg2.ProgrammingError):
        cursor.close()
        return []