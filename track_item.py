# enter item url
# confirm the item
# every x minutes, get the price. If it is below a certain price, send an email
# use crontab to run regularly
import time

from constants import ITEM
from parse.create_pricehistory import create_pricehistory_instance
from search.amazon.search import get_item_price
from search.website import go_to_website, init_driver


def the_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print(current_time)


def record_price(browser, url):
    """Return a PriceHistory instance from a URL"""
    # go to website
    go_to_website(browser, url)

    # parse data from page
    price_string = get_item_price(browser)

    # create PriceHistory
    data = create_pricehistory_instance(url, price_string)
    print(data)
    return data


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
    print("test")
    main()
    # https://stackoverflow.com/questions/474528/what-is-the-best-way-to-repeatedly-execute-a-function-every-x-seconds
    # json file recordwed as bytes, decode it
