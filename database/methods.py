from database.data_classes import Alerts, Items, Price_History, User

#################
# conn = psycopg2.connect(host="localhost", database="mydb", user="zaki", password="password123")


def return_user(conn, email):
    cur = conn.cursor()
    cur.execute("SELECT * FROM webscrape.users WHERE email = %s", (email,))
    return cur.fetchone()


def add_user(conn, person: User):
    """add user to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.users (email, password) VALUES (%s, %s)",
        (person.email, person.password),
    )
    cur.close()
    return


def add_item(conn, item: Items):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.items (asin, title, current_amount, currency) VALUES (%s, %s, %s, %s)",
        (item.asin, item.title, item.current_amount, item.currency),
    )
    cur.close()
    return


def add_alert(conn, alert: Alerts):
    """add alert to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.alerts (asin, id, target_amount) VALUES (%s, %s, %s)",
        (alert.asin, alert.id, alert.target_amount),
    )
    cur.close()
    return


def add_price_history(conn, ph: Price_History):
    """add ph to db"""
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO webscrape.price_history (asin, date, amount, currency) VALUES (%s, %s, %s, %s)",
        (ph.asin, ph.date, ph.amount, ph.currency),
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


# sort out uniques in db
# https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
