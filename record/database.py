import datetime
import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from typing import Tuple

from classes import Database, PriceHistory


# change database structure,
def init_database(address: str = ":memory:") -> Tuple[Cursor, Connection]:
    """Open connection to the database, and return a cursor & connection"""
    con = sqlite3.connect(address)
    cur = con.cursor()
    return (cur, con)


def add_to_item_database(cur: Cursor, item: PriceHistory):
    # look into sqlalchemy for python/db interaction
    cur.execute(
        "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
        {
            "name": item.name,
            "date": item.date,
            "price": item.price,
            "currency": item.currency,
            "trend": item.trend,
        },
    )
    return


def test():
    with Database() as db:
        db.cur.execute(
            """CREATE TABLE IF NOT EXISTS items (
            name text,
            date text,
            price real,
            currency text,
            trend integer
            )"""
        )
        db.cur.execute(
            "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
            {
                "name": "coffee",
                "date": "2021-11-15",
                "price": 5.20,
                "currency": "£",
                "trend": -1,
            },
        )
        db.cur.execute(
            "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
            {
                "name": "coffee",
                "date": "2021-11-16",
                "price": 5.20,
                "currency": "£",
                "trend": -1,
            },
        )
        db.cur.execute(
            "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
            {
                "name": "coffee",
                "date": "2021-11-1",
                "price": 5.20,
                "currency": "£",
                "trend": -1,
            },
        )
        db.cur.execute(
            "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
            {
                "name": "coffee",
                "date": datetime.datetime.now(),
                "price": 5.39,
                "currency": "£",
                "trend": -1,
            },
        )
        data = db.cur.execute("SELECT * FROM items")
        print(data.fetchall())
    return


if __name__ == "__main__":
    print(datetime.datetime.now())
