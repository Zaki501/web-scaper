import psycopg2

from database.methods import return_user


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
        "CREATE TABLE IF NOT EXISTS webscrape.users ("
        "id serial,"
        "email text,"
        "password text,"
        "PRIMARY KEY (id),"
        "UNIQUE (email)"
        ")"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS webscrape.items("
        "asin text,"
        "title text,"
        "current_amount numeric(6,2),"
        "currency text,"
        "PRIMARY KEY (asin)"
        ")"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS webscrape.alerts ("
        "asin text REFERENCES webscrape.items (asin),"
        "id serial REFERENCES webscrape.users (id),"
        "target_amount numeric(6, 2)"
        ")"
    )
    cur.execute(
        "CREATE TABLE IF NOT EXISTS webscrape.price_history ("
        "asin text REFERENCES webscrape.items (asin),"
        "date date,"
        "amount numeric(6, 2),"
        "currency text"
        ")"
    )

    cur.close()
    return


def get_alerts_to_email(conn):
    cur = conn.cursor()
    # three table join
    cur.execute(
        """
    SELECT users.email, alerts.asin, items.title, items.current_amount, alerts.target_amount
    FROM webscrape.users
    INNER JOIN webscrape.alerts ON users.id=alerts.id
    INNER JOIN webscrape.items ON alerts.asin=items.asin
    WHERE items.current_amount > alerts.target_amount
    """
    )
    # for person in full_list:
    #     (email, asin, title, current_amount, target_amount) = person
    #     print(current_amount)

    return cur.fetchall()


if __name__ == "__main__":

    conn = init_connection()
    # create_schema(conn)
    # create_tables(conn)
    # mock_data(conn)
    # a = get_alerts_to_email(conn)
    # print(a)

    a = return_user(conn, "tm@gmail.com")
    # print(a)
    if a:
        print("user exists")
    else:
        print("no user")
    conn.close()
