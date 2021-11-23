from dataclasses import dataclass
from datetime import datetime

from database import compare_to_previous_amount
from price_parser import parse_price


@dataclass
class PriceHistory:
    name: str
    date: str
    price: float
    currency: str
    trend: int


def get_float_amount_and_currency(price_string):
    """Return the price as a float and currency symbol as a string"""
    price = parse_price(price_string)
    return (float(price.amount), price.currency)


# get the data first, then pass it in
# go_to_website(browser, url)


def create_pricehistory_instance(url, price_string):
    """Return a PriceHistory instance from a URL and price string"""

    # parse data from page
    # price = get_item_price(browser)
    (amount, currency) = get_float_amount_and_currency(price_string)
    trend = compare_to_previous_amount(url, amount)

    return PriceHistory(
        name=url,
        date=datetime.now(),
        price=amount,
        currency=currency,
        trend=trend,
    )


if __name__ == "__main__":
    print(datetime.now())
