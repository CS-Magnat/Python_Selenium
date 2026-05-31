import time

from pages.base_page import BasePage


def test(driver):
    page = BasePage(driver, "https://example.com")
    page.open()
    time.sleep(5)