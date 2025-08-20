import pytest

@pytest.mark.smoke
def test_login_success(login_page):
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.flash_message()

def test_login_fail(login_page):
    login_page.login("tomsmith", "wrong")
    assert "Your password is invalid!" in login_page.flash_message()
