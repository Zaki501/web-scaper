# main functions, to be imported to app
# track item(asin) -> PriceHistory, sent to DB
# regular tracking -> list of asins, for each item,
import re

from constants import AMAZON
from FirefoxWebDriver import FireFoxBrowser
from PriceHistory import PriceHistory


def extract_asin(url: str):
    """Extract asin from url"""
    asin = re.search("/[dg]p/([^/]+)", url, flags=re.IGNORECASE)
    if asin is None:
        raise ValueError("No asin found in Url")
    return asin.group(1)


def item_confirmation(url: str) -> str:
    """Return img src, title and price string"""

    ## if confirmed add item with asin to database
    pass


def track_item(browser: FireFoxBrowser, asin: str):
    """Get data for one amazon item"""
    address = f"{AMAZON}{asin}"
    browser.get(address)
    # change pricehistory to take in driver and asin
    return PriceHistory(browser, asin)


def regular_tracking(list_of_asins):
    # This will be ran once a day
    # get list of all asins from database
    # for each asin:
    #   open browser, and create pricehistory
    #   close browser
    #   open database
    #   add to database
    #   close
    #   sleep for n seconds

    # error if item isnt availible
    # custon excpetions

    # list of asins will be taken from database

    for asin in list_of_asins:
        browser = FireFoxBrowser(headless=False, random_user_agent=True)
        with browser:

            item = track_item(browser, asin)
            item.__dict__

            # output list of pricehistory, add to database (use sqlalchemy)

    pass


if __name__ == "__main__":
    x = "https://www.amazon.co.uk/dp/B07PPTN43Y"
    browser = FireFoxBrowser(headless=False, random_user_agent=True)
    with browser:
        asin = extract_asin(x)
        item = track_item(browser, asin)
        print(item.__dict__)
    pass
