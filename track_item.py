# enter item url
# confirm the item
# every x minutes, get the price. If it is below a certain price, send an email
# use crontab to run regularly
import time
from dataclasses import dataclass
from datetime import datetime

from price_parser import parse_price

from amazon.item_tracker.database import compare_to_previous_amount
from amazon.web_scraper.search import get_item_price
from constants import ITEM
from website import go_to_website, init_driver


@dataclass
class PriceHistory:
    name: str
    date: str
    price: float
    currency: str
    trend: int


# asdict( class instance )


def the_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)


def get_float_amount_and_currency(price_string):
    """Return the price as a float and currency symbol as a string"""
    price = parse_price(price_string)
    return (float(price.amount), price.currency)


def record_price(browser, url):
    """Return a PriceHistory instance from a URL"""
    # go to website
    go_to_website(browser, url)

    # parse data from page
    price = get_item_price(browser)
    (amount, currency) = get_float_amount_and_currency(price)
    trend = compare_to_previous_amount(url)

    return PriceHistory(
        name=url,
        date=datetime.datetime.now(),
        price=amount,
        currency=currency,
        trend=trend,
    )


def main():
    # setup (first time running):
    # enter and confirm the item
    # choose target price
    # setup the cronjob for regular price check

    # recurring:
    # go to address
    # grab price
    # create class instance: url, date, price, currency, trend
    # send email when it goes below target price
    the_time()
    browser = init_driver()
    record_price(browser, ITEM)
    print("~ DONE")
    return


if __name__ == "__main__":
    # main()
    print("test")
    # https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds
    # json file recordwed as bytes, decode it
