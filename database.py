from dataclasses import dataclass
from decimal import Decimal

import psycopg2


@dataclass
class User:
    email: str
    password: str


@dataclass
class Alert:
    asin: str
    email: str


@dataclass
class Price_History:
    asin: str
    title: str
    date: str
    amount: Decimal
    currency: str


#################
# conn = psycopg2.connect(host="localhost", database="mydb", user="zaki", password="password123")


def psql_create_db():
    """
    CREATE DATABASE mydb;
    CREATE USER zaki with encrypted password 'password123';
    GRANT ALL PRIVILEGES ON DATABASE mydb TO zaki;
    """
    """
    The database should be manually created in psql using the above.
    After that, the code below will create the schema and tables.
    """


def init_connection():
    conn = psycopg2.connect(
        host="localhost", database="mydb", user="zaki", password="password123"
    )
    conn.autocommit = True
    return conn


def new_schema(conn):
    """After manually creating and setting up psql database, run this"""
    cur = conn.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS webscrape AUTHORIZATION zaki")
    cur.close()


def create_table(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS webscrape.test (name text, age integer)")
    cur.close()


def list_of_asins(conn):
    # the asins have empty space, caused by the psql table defintions
    """with db open, extract list of asins from Alerts, return list"""
    cur = conn.cursor()
    cur.execute("SELECT asin FROM webscrape.alerts")
    x = [i[0] for i in cur.fetchall()]
    cur.close()
    return x


def add_alert(conn, Alert: Alert):
    """add user to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.alerts (asin, email) VALUES (%s, %s)",
        (Alert.asin, Alert.email),
    )
    cur.close()


def add_price_history(conn, ph: Price_History):
    """add ph to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.price_history (asin, title, date, amount, currency) VALUES (%s, %s, %s, %s, %s)",
        (ph.asin, ph.title, ph.date, ph.amount, ph.currency),
    )
    # conn.commit()
    cur.close()
    return


def mock_data(conn):
    will = Alert(asin="B07SVVP426", email="will@gmail.com")
    tom = Alert(asin="B00OLZXQTM", email="tom@gmail.com")
    add_alert(conn, will)
    add_alert(conn, tom)
    item1 = Price_History(
        asin="B07SVVP426",
        title="Natural Magnesium Glycinate 500mg Premium Quality Ideal Strength 100 Vegan Capsules Highest Bioavailability",
        date="2022-01-29",
        amount=9.97,
        currency="£",
    )
    item2 = Price_History(
        asin="B00OLZXQTM",
        title="Dexam 17819184 Vintage Home Enamelware 400ml Turkish Coffee Pot, Claret Red",
        date="2022-01-29",
        amount=925.0,
        currency="£",
    )
    add_price_history(conn, item1)
    add_price_history(conn, item2)


def mock_table(conn):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.test (name, age) VALUES (%s, %s)", ("timonthy", 34)
    )
    cur.close()


def print_table(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM webscrape.test")
    a = cur.fetchall()
    print(a)
    cur.close()


if __name__ == "__main__":
    # conn = init_connection()
    # add ALERT data, currently not commited
    # mock_data(conn)
    # x = list_of_asins(conn)
    # # this still has empty spaces, psql table defintions
    # for item in x:
    #     print("sdfd")
    #     print(item)
    # pass
    # cur = conn.cursor()
    # cur.execute("SELECT * from webscrape.price_history")
    # p = cur.fetchall()
    # print(p)

    conn = init_connection()
    new_schema(conn)
    create_table(conn)
    # mock_data(conn)
    mock_table(conn)
    print_table(conn)
    conn.close()


# https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
