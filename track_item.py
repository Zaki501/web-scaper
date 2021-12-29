from classes import Database
from constants import DB_PATH
from parse.create_pricehistory import create_pricehistory
from record.database import add_to_item_database
from search.amazon.search import (
    _get_item_price,
    _validate_amazon_url,
    amazon_address,
    create_amazonurl,
    get_confirmation_data,
)
from search.website import go_to_website, init_driver, url_validator


def regular_tracking(url: str):
    """If valid URl, and its amazon URl, Run this function"""
    # User Enters a Url
    # Go to amazon page, take ImgSRC, title and Price
    # send image/title/price, so user can confirm
    # if correct, store data, and begin recurring price check

    ## Go to valid url
    # validate address
    address = create_amazonurl(url)
    if not url_validator(address):
        raise ValueError("Invalid Url - Please enter a full address")

    ## Scrape data
    with init_driver() as browser:
        # Go to website, scrape data
        go_to_website(browser, address.string)
        price_string = _get_item_price(browser)

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


def item_confirmation(url: str) -> str:
    """Return img src, title and price string"""
    # confirm valid amazon url
    _validate_amazon_url(url)
    # open driver, go to website
    with init_driver() as browser:
        go_to_website(browser, url)
        data = get_confirmation_data(browser)
    # extract and return data
    return data


def track_item_main(url: str):
    # enter url
    if not amazon_address(url):
        print("respond with invalid address")


if __name__ == "__main__":
    # begin_tracking(ITEM)
    # pass
    a = "https://www.amazon.co.uk/gp/product/B01GVLNUO4/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1"
    # x = item_confirmation(a)
    # print(x)
    _validate_amazon_url(a)
