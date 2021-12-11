from classes import Database
from constants import DB_PATH, ITEM
from parse.create_pricehistory import create_pricehistory
from record.database import add_to_item_database
from search.amazon.search import get_item_price
from search.website import go_to_website, init_driver, parse_url, url_validator


def begin_tracking(url: str):
    """If the item is not found in the database, run this func"""
    # (optional) confirm item
    # sqlite3 - one table for item + id, another for pricehistory

    ## Go to valid url
    # validate address
    address = parse_url(url)
    if not url_validator(address):
        raise ValueError("Invalid Url - Please enter a full address")

    ## Scrape data
    with init_driver() as browser:
        # Go to website, scrape data
        go_to_website(browser, address.string)
        price_string = get_item_price(browser)

    ## Parse and record Data
    with Database(DB_PATH) as db:
        data = create_pricehistory(db.cur, address.string, price_string)
        # if sql table doesnt exis, create it
        db.cur.execute(
            """CREATE TABLE IF NOT EXISTS items (
            name text,
            date text,
            price real,
            currency text,
            trend integer
            )"""
        )
        # add pricehistory to table
        add_to_item_database(db.cur, data)
        x = db.cur.execute("SELECT * FROM items")
        print(x.fetchall())

    print(data)
    print("///DONE")
    return


if __name__ == "__main__":
    begin_tracking(ITEM)
    # print(datetime.datetime.now().strftime("%Y-%m-%d"))
    pass
