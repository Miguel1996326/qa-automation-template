import pytest
from src.utils.driver import build_driver
from src.pages.login_page import LoginPage
from src import config

@pytest.fixture
def driver():
    drv = build_driver(config.HEADLESS)
    yield drv
    drv.quit()

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open_login(config.BASE_URL)
    return page
