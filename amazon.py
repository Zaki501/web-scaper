def search_amazon_item(driver, item):
    """Search for an item in amazon"""
    search_bar = driver.find_element_by_id("twotabsearchtextbox")
    search_button = driver.find_element_by_id("nav-search-submit-button")

    search_bar.send_keys(item)
    driver.implicitly_wait(3)
    search_button.click()
    return


def get_item_data(driver):
    """Grab the item data"""
    # items_container = driver.find_elements_by_xpath("//div[@class='s-main-slot s-result-list']")
    # items = driver.find_elements_by_xpath("//div[@class='s-result-item s-asin']")
    items_container = driver.find_elements_by_css_selector(".s-main-slot.s-result-list")
    items = driver.find_elements_by_css_selector(".s-result-item.s-asin")
    print(items_container, items)
    return (items_container, items)


def get_element_text(item_list):
    # new_list = []
    # for idx, element in item_list:
    #     return {idx: element.text}
    return [{idx: element.text} for (idx, element) in enumerate(item_list)]


# driver.find_elements_by_class_name("")
# driver.find_elements_by_class_name("")

# driver.find_elements_by_css_selector(". sfibbbc. jsb")
# //*[@id="nav-search-submit-button"]
# search_bar.send_keys(Keys.ENTER)f
