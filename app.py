import argparse
import re
import sys

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def parse_args():
    """returns the parse arguments"""
    parser = argparse.ArgumentParser(description="Screenshot a website.")
    parser.add_argument("address", type=str, help="a web URL")
    args = parser.parse_args()
    return args


def valid_address(url: str):
    """Checks for http/https format."""
    return bool(re.search("http", url))


def screenshot_website(browser, url: str):
    """Screenshot site"""
    browser.get(url)
    browser.get_screenshot_as_file("output.png")


def main():

    """Main function"""
    user_input = parse_args()
    url = user_input.address
    if not valid_address(url):
        sys.exit("Invalid input - use http/https")

    print("test")

    path = "/usr/bin/geckodriver"
    options = Options()
    options.headless = True
    browser = webdriver.Firefox(executable_path=path, options=options)

    screenshot_website(browser, user_input.address)

    browser.quit()

    print("> Done")


if __name__ == "__main__":
    main()
# check if input matches condition
# regex = '/^(https?:\/\/)/i'
