import re
import sys


def _valid_address(url: str) -> bool:
    """Checks for http/https format."""
    return bool(re.search("http", url))


def go_to_website(browser, url):
    """Check if the website is valid, then goes to it"""
    if not _valid_address(url):
        sys.exit("Invalid input - use http/https")
    browser.get(url)


def take_screenshot(browser, url: str):
    """Screenshot the current browser"""
    browser.get_screenshot_as_file("output.png")


def go_to_website_and_take_screenshot(url, browser):
    """Go to a website, screenshot it, then exit"""
    go_to_website(url)
    print("Getting Screenshot...")
    take_screenshot(browser, url)
    print("Screenshot saved")
    browser.quit()


if __name__ == "__main__":
    print("screenshot file")
