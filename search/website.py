import re
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from constants import PATH_TO_DRIVER


def init_driver():
    print("configure program")
    options = Options()
    # options.headless = True
    driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER, options=options)
    print("start")
    return driver


def _valid_address(url: str) -> bool:
    """Checks for http/https format."""
    return bool(re.search("http", url))


def go_to_website(browser, url):
    """Check if the website is valid, then goes to it"""
    if not _valid_address(url):
        sys.exit("Invalid input - use http/https")
    browser.get(url)


def take_screenshot(browser, output_file):
    """Screenshot the current browser"""
    browser.get_screenshot_as_file(output_file)


def go_to_website_and_take_screenshot(url, browser):
    """Go to a website, screenshot it, then exit"""
    go_to_website(url)
    print("Getting Screenshot...")
    take_screenshot(browser, url)
    print("Screenshot saved")
    browser.quit()


def get_element_text(item_list):
    # new_list = []
    # for idx, element in item_list:
    #     return {idx: element.text}
    return [{idx: element.text} for (idx, element) in enumerate(item_list)]


if __name__ == "__main__":
    print("test save to txt file:")
