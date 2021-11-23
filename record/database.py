import datetime
import sqlite3


def compare_to_previous_amount(url, current_amount):
    """Returns a bool to represent price trend"""

    # search for latest entry
    a = cur.execute(
        "SELECT price FROM items WHERE name=:name ORDER BY date DESC LIMIT 1",
        {"name": url},
    )
    list = a.fetchall()

    # check for previous entries in database
    if not list:
        print("first entry in database: trend = 0")
        return 0

    # convert tuple in list, to float
    item = [x[0] for x in list]
    (previous_amount,) = item

    # compare prices
    if current_amount > previous_amount:
        return 1
    elif current_amount == previous_amount:
        return 0
    else:
        return -1


con = sqlite3.connect(":memory:")

cur = con.cursor()

# Create table
# trend: price goes down (-1), no change (0), goes up (1)

cur.execute(
    """CREATE TABLE items (
    name text,
    date text,
    price real,
    currency text,
    trend integer
    )"""
)

# Insert a row of data
cur.execute(
    "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
    {
        "name": "coffee",
        "date": "2021-11-15",
        "price": 5.20,
        "currency": "£",
        "trend": -1,
    },
)
cur.execute(
    "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
    {
        "name": "coffee",
        "date": "2021-11-16",
        "price": 5.20,
        "currency": "£",
        "trend": -1,
    },
)
cur.execute(
    "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
    {
        "name": "coffee",
        "date": "2021-11-1",
        "price": 5.20,
        "currency": "£",
        "trend": -1,
    },
)
cur.execute(
    "INSERT INTO items VALUES (:name, :date, :price, :currency, :trend)",
    {
        "name": "coffee",
        "date": datetime.datetime.now(),
        "price": 5.39,
        "currency": "£",
        "trend": -1,
    },
)

# Save (commit) the changes
con.commit()

# cur.execute("SELECT * FROM items WHERE name=:name", {'name': 'coffee'})
# print(cur.fetchall())
# a = cur.execute(
#     "SELECT PRICE FROM items WHERE name=:name ORDER BY date DESC LIMIT 1",
#     {"name": "coffee"},
# )
# b = a.fetchall()

# print(b)
print("init database")

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()
