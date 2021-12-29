import re

from selenium.webdriver.firefox.webdriver import WebDriver

from classes import AmazonUrl, ItemData


def amazon_address(url: str) -> bool:
    """Checks for http/https format."""
    return bool(re.search("amazon", url))


def get_item_search_data(driver: WebDriver):
    """After searching for an item, get all the text for each result"""
    items_container = driver.find_elements_by_css_selector(".s-main-slot.s-result-list")
    items = driver.find_elements_by_css_selector(".s-result-item.s-asin")
    print(items_container, items)
    return (items_container, items)


def search_item(driver: WebDriver, item: str):
    """Search for an item in amazon"""
    search_bar = driver.find_element_by_id("twotabsearchtextbox")
    search_button = driver.find_element_by_id("nav-search-submit-button")
    search_bar.send_keys(item)
    driver.implicitly_wait(3)
    search_button.click()
    return


def _get_item_price(driver: WebDriver):
    """On items page, get the text data"""
    # title =  driver.find_element_by_id('productTitle')
    price = driver.find_element_by_css_selector(".a-price")
    return price.text


def _get_item_title(driver: WebDriver):
    """Return item title"""
    return driver.find_element_by_id("productTitle").text


def _validate_amazon_url(url: str):
    """Checks for asin in Url
    Throws error if there isn't"""
    asin = re.search("/[dg]p/([^/]+)", url, flags=re.IGNORECASE)
    if asin is None:
        raise ValueError("No asin found in Url")


def _get_amazon_asin(url: str) -> str:
    """Checks if user url has an asin
    (10digit number id, that all amazon items have)"""

    asin = re.search("/[dg]p/([^/]+)", url, flags=re.IGNORECASE)
    if asin is None:
        raise ValueError("No asin found in Url")
    return asin.group(1)


def _get_image_src(driver: WebDriver):
    return driver.find_element_by_id("landingImage").get_attribute("src")


def create_amazonurl(driver: WebDriver, url: str) -> AmazonUrl:
    # check if url contains amazon first
    """Will attempt to create a AmazonUrl class instance.
    Check if it throws exception (Optional str)"""
    asin = _get_amazon_asin(url)
    title = _get_item_title(driver)
    image_src = _get_image_src(driver)
    price_string = _get_item_price(driver)
    return AmazonUrl(
        string=url, asin=asin, title=title, image_src=image_src, price=price_string
    )


def get_confirmation_data(driver: WebDriver) -> ItemData:
    """Return Image, title, price"""
    img = _get_image_src(driver)
    title = _get_item_title(driver)
    price = _get_item_price(driver)
    return ItemData(
        img_src=img,
        title=title,
        price=price,
    )


if __name__ == "__main__":
    x = "https://www.amazon.co.uk/Vitamin-Maximum-Strength-Supplement-Softgels/dp/B072L235Z5/ref=sr_1_5?keywords=vitamin+d&qid=1637159981&sr=8-5"
    asin = _get_amazon_asin(x)
    q = amazon_address(x)
    print(q)
