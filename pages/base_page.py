# pages/base_page.py
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def load(self, url):
        self.browser.get(url)

    def find_element(self, locator):
        return self.browser.find_element(*locator)

    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    def click(self, locator):
        self.find_element(locator).click()