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
    target_amount: Decimal


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
    CREATE USER <name> with encrypted password '<password>';
    GRANT ALL PRIVILEGES ON DATABASE mydb TO <name>;
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


def create_schema(conn):
    """After manually creating and setting up psql database, run this"""
    cur = conn.cursor()
    cur.execute("CREATE SCHEMA IF NOT EXISTS webscrape AUTHORIZATION zaki")
    cur.close()
    return


def create_tables(conn):
    """look into storing passwords, and its hashes"""
    cur = conn.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS webscrape.test (name text, age integer)")
    cur.execute(
        "CREATE TABLE IF NOT EXISTS webscrape.users "
        "(email text, password text)"
        ""
        ""
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS webscrape.alerts "
        "(email text, asin text, target_amount numeric(6, 2))"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS webscrape.price_history "
        "(asin text, title text, date date, amount numeric(6, 2), currency text)"
    )
    cur.close()
    return


def list_of_unique_asins(conn):
    # the asins have empty space, caused by the psql table defintions
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT asin FROM webscrape.alerts")
    x = [i[0] for i in cur.fetchall()]
    cur.close()
    return x


def add_alert(conn, alert: Alert):
    """add alert to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.alerts (asin, email, target_amount) VALUES (%s, %s, %s)",
        (alert.asin, alert.email, alert.target_amount),
    )
    cur.close()
    return


def add_price_history(conn, ph: Price_History):
    """add ph to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.price_history (asin, title, date, amount, currency) VALUES (%s, %s, %s, %s, %s)",
        (ph.asin, ph.title, ph.date, ph.amount, ph.currency),
    )
    cur.close()
    return


def add_user(conn, person: User):
    """add user to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.users (email, password) VALUES (%s, %s)",
        (person.email, person.password),
    )
    cur.close()
    return


def mock_data(conn):
    # mock alert
    will = Alert(asin="B07SVVP426", email="will@gmail.com", target_amount=Decimal(6.5))
    tom = Alert(asin="B00OLZXQTM", email="tom@gmail.com", target_amount=Decimal(5.24))
    add_alert(conn, will)
    add_alert(conn, tom)
    # mock pricehistory
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
    # mock user
    person1 = User(email="will@gmail.com", password="password123")
    person2 = User(email="tom@gmail.com", password="password123")
    add_user(conn, person1)
    add_user(conn, person2)
    return


def print_table(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM webscrape.alerts")
    a = cur.fetchall()
    print(a)
    cur.close()
    return


"""
Database notes:

add to database:
alerts: email, asin, and target price DONE
user: make email unique

all database interactions:
front end:
    user (email, password):
        current asins and target price
        change email/password
    alerts (email, asin, target price):
        add/remove asin
        change target price

Change to tables:
    add target price to Alerts

database queries:
    Automated back-end
        - select all unique asins (for price history backend function)  DONE
        - select all grouped emails associated with each unique asin,
            the target price for each email, and its latest price from price history
            (then send emails)

    get all asins in alert, and its current price
    get all emails/target_price attached to unique asin (alerts), and current amount (ph) -> join alerts and p_h on asin
    - given a user, select all asins and current/target price, associated with an email (for displaying at user front end)

emailing:
    for each unique asin in alerts:
        get current price
        for each id tracking asin:
            if tracking price <= target price
                send email

"""

if __name__ == "__main__":

    conn = init_connection()
    # create_schema(conn)
    # create_tables(conn)
    # mock_data(conn)
    # print_table(conn)
    a = list_of_unique_asins(conn)
    print(a)
    conn.close()
    # cur = conn.cursor()
    # cur.execute()


# sort out uniques in db
# https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
