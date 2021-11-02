import re

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from amazon import search_amazon_item
from constants import PATH_TO_DRIVER
from parse_arguments import parse_args
from screenshot import go_to_website, take_screenshot


def main():
    # Configure arguments
    args = parse_args()

    # Configure selenium
    print("configure program")
    options = Options()
    # options.headless = True
    driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER, options=options)

    # start program
    print("start")

    if bool(re.search("amazon", args.address)):
        go_to_website(driver, args.address)
        print("going to amazon")
        search_amazon_item(driver, "rx 580")

    if args.screenshot is True:
        print("taking a screenshot")
        take_screenshot(driver, args.address)
    else:
        print("no screenshot")

    # driver.quit()
    print("quit and done")


if __name__ == "__main__":
    main()

# args = parse_args()
# main(*args)
# https://www.reddit.com/r/learnpython/comments/3do2wr/where_to_put_argparse/

# screen shot arg as bool
# parse args, then pass *args into main

# uk covid historical data -> https://coronavirus.data.gov.uk/details/download
# scrape amazon/ebay -> track price of item (e.g gpu)
