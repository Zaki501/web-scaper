"""
    Methods to insert and query data in psql db
"""
import psycopg2
from models import Alert, Price_History

# conn = psycopg2.connect(host="localhost", database="mydb", user="zaki", password="password123")


def init_connection():
    return psycopg2.connect(
        host="localhost", database="mydb", user="zaki", password="password123"
    )


def list_of_asins(conn):
    # the asins have empty space, caused by the psql table defintions
    """with db open, extract list of asins from Alerts, return list"""
    cur = conn.cursor()
    cur.execute("SELECT asin FROM webscrape.alerts")
    return [i[0] for i in cur.fetchall()]


def add_alert(conn, Alert: Alert):
    """add user to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.alerts (asin, email) VALUES (%s, %s)",
        (Alert.asin, Alert.email),
    )
    return


def add_price_history(conn, ph: Price_History):
    """add ph to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.price_history (asin, title, date, amount, currency) VALUES (%s, %s, %s, %s, %s)",
        (ph.asin, ph.title, ph.date, ph.amount, ph.currency),
    )
    conn.commit()
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
    item2 = {
        "asin": "B00OLZXQTM  ",
        "title": "Dexam 17819184 Vintage Home Enamelware 400ml Turkish Coffee Pot, Claret Red",
        "date": "2022-01-29",
        "amount": 925.0,
        "currency": "£",
    }
    add_price_history(conn, item1)
    add_price_history(conn, item2)


if __name__ == "__main__":
    conn = init_connection()
    # add ALERT data, currently not commited
    mock_data(conn)
    x = list_of_asins(conn)
    # this still has empty spaces, psql table defintions
    for item in x:
        print(item)
    pass

# https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
