from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from amazon.web_scraper.search import (
    get_element_text,
    get_item_search_data,
    search_amazon_item,
)
from constants import AMAZON, PATH_TO_DRIVER
from parse_arguments import parse_args
from save_data import save_to_json_file, save_to_text_file
from website import go_to_website, take_screenshot


def main(args):
    print(args)
    # Configure selenium
    print("configure program")
    options = Options()
    # options.headless = True
    driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER, options=options)

    ## start program
    # search for item
    print("start")

    go_to_website(driver, AMAZON)
    search_amazon_item(driver, args.item)

    # Printing the whole body text
    text = driver.find_element_by_xpath("/html/body").text
    save_to_text_file(text, "output/data.txt")

    # testing element selection
    (items_container, items) = get_item_search_data(driver)
    list_of_element_text = get_element_text(items)
    save_to_text_file(items_container, "output/item_container.txt")
    save_to_json_file(list_of_element_text, "output/items.json")

    if args.screenshot is True:
        print("taking a screenshot")
        take_screenshot(driver, "output/output.png")
    else:
        print("no screenshot")

    # driver.quit()
    print(">Done")


if __name__ == "__main__":
    args = parse_args()
    main(args)

# if bool(re.search("amazon", args.address)):
#     go_to_website(driver, args.address)
#     print("going to amazon")
#     search_amazon_item(driver, "rx 580")
