from datetime import datetime
from sqlite3.dbapi2 import Cursor
from typing import Tuple

from price_parser import parse_price

from classes import PriceHistory


def get_float_amount_and_currency(price_string: str) -> Tuple[float, str]:
    """Return the price as a float and currency symbol as a string"""
    price = parse_price(price_string)
    return (float(price.amount), price.currency)


# get the data first, then pass it in
# go_to_website(browser, url)


def compare_to_previous_amount(cursor: Cursor, url: str, current_amount: float) -> int:
    """Returns a bool to represent price trend"""

    # search for latest entry
    list = cursor.execute(
        "SELECT price FROM items WHERE name=:name ORDER BY date DESC LIMIT 1",
        {"name": url},
    ).fetchall

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


def create_pricehistory(cursor: Cursor, url: str, price_string: str) -> PriceHistory:
    """Return a PriceHistory instance from a URL and price string"""

    # parse data from page
    # price = get_item_price(browser)
    (amount, currency) = get_float_amount_and_currency(price_string)
    # trend = compare_to_previous_amount(cursor, url, amount)
    trend = 2

    return PriceHistory(
        name=url,
        date=datetime.now().strftime("%Y-%m-%d"),
        price=amount,
        currency=currency,
        trend=trend,
    )


if __name__ == "__main__":
    print(datetime.now())
