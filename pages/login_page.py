# pages/login_page.py
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'Email')
    PASSWORD_FIELD = (By.ID, 'Password')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button')

    def login(self, username, password):
        self.input_text(self.USERNAME_FIELD, username)
        self.input_text(self.PASSWORD_FIELD, password)
        self.click(self.SUBMIT_BUTTON)