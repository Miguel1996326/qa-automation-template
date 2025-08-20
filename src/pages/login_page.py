from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    BTN_LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")

    def open_login(self, base_url: str):
        self.open(f"{base_url}/login")

    def login(self, user: str, pwd: str):
        self.type(self.USERNAME, user)
        self.type(self.PASSWORD, pwd)
        self.click(self.BTN_LOGIN)

    def flash_message(self) -> str:
        return self.text_of(self.FLASH)
