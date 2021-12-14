import re
from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.webdriver import WebDriver

from classes import Url
from constants import ITEM, PATH_TO_DRIVER


def init_driver() -> WebDriver:
    print("configure browser")
    s = Service(PATH_TO_DRIVER)
    options = Options()
    # options.headless = True
    driver = webdriver.Firefox(service=s, options=options)
    print("start")
    return driver


def _valid_address(url: str) -> bool:
    """Checks for http/https format."""
    return bool(re.search("http", url))


def url_validator(address: Url) -> bool:
    try:
        # result = urlparse(address)
        return all([address.scheme, address.netloc, address.path])
    except Exception as e:
        # TODO
        # flake8 error - E722 do not use bare 'except'
        print(e)
        return False


def parse_url(url: str) -> Url:
    """Will attempt to create a Url class instance.
    Check if it throws exception (Optional str)"""
    x = urlparse(url)
    return Url(
        string=url,
        scheme=x.scheme,
        netloc=x.netloc,
        path=x.path,
        params=x.params,
        query=x.query,
    )


def go_to_website(browser: WebDriver, url: str):
    """Check if the website is valid, then goes to it"""
    # if not _valid_address(url):
    #     sys.exit("Invalid input - use http/https")
    browser.get(url)


def take_screenshot(browser: WebDriver, output_file):
    """Screenshot the current browser"""
    browser.get_screenshot_as_file(output_file)


def go_to_website_and_take_screenshot(browser: WebDriver, url: str):
    """Go to a website, screenshot it, then exit"""
    go_to_website(url)
    print("Getting Screenshot...")
    take_screenshot(browser, url)
    print("Screenshot saved")
    browser.quit()


# def get_element_text(item_list):
#     # new_list = []
#     # for idx, element in item_list:
#     #     return {idx: element.text}
#     return [{idx: element.text} for (idx, element) in enumerate(item_list)]


def test():
    s = parse_url(ITEM)
    print(s)


if __name__ == "__main__":
    # x = init_driver()
    # print(type(x))
    pass
