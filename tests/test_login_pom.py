
from pages.login_page import LoginPage


def test_valid_login(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    assert page.url.endswith("/inventory.html")


def test_locked_user(page):

    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "locked_out_user",
        "secret_sauce"
    )

    assert "locked out" in login_page.get_error_message()
