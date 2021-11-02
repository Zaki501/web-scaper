def search_amazon_item(driver, item):
    """Search for an item in amazon"""
    search_bar = driver.find_element_by_id("twotabsearchtextbox")
    search_button = driver.find_element_by_id("nav-search-submit-button")

    search_bar.send_keys(item)
    driver.implicitly_wait(3)
    search_button.click()

    # search_bar.send_keys(Keys.ENTER)


# go to amazon.co.uk
# search for an item
# wait for it to load!!
# take a screenshot
# //*[@id="nav-search-submit-button"]
