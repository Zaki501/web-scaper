def search_item(driver, item):
    """Search for an item in amazon"""
    search_bar = driver.find_element_by_id("twotabsearchtextbox")
    search_button = driver.find_element_by_id("nav-search-submit-button")

    search_bar.send_keys(item)
    driver.implicitly_wait(3)
    search_button.click()
    return


def get_item_price(driver):
    """On items page, get the text data"""
    # title =  driver.find_element_by_id('productTitle')
    price = driver.find_element_by_css_selector(".a-price")
    return price.text


def get_item_search_data(driver):
    """After searching for an item, get all the text for each result"""

    items_container = driver.find_elements_by_css_selector(".s-main-slot.s-result-list")
    items = driver.find_elements_by_css_selector(".s-result-item.s-asin")
    print(items_container, items)
    return (items_container, items)


# driver.find_elements_by_class_name("")
# driver.find_elements_by_class_name("")

# driver.find_elements_by_css_selector(". sfibbbc. jsb")
# //*[@id="nav-search-submit-button"]
# search_bar.send_keys(Keys.ENTER)f
