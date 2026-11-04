
import pytest


@pytest.mark.parametrize(
    "username, password, expected_result",
    [
        ("standard_user", "secret_sauce", "success"),
        ("locked_out_user", "secret_sauce", "locked"),
        ("problem_user", "secret_sauce", "success")
    ]
)
def test_login(page, username, password, expected_result):

    page.goto("https://www.saucedemo.com/")

    page.locator("#user-name").fill(username)
    page.locator("#password").fill(password)

    page.locator("#login-button").click()

    if expected_result == "success":

        assert page.url.endswith("/inventory.html")

    elif expected_result == "locked":

        error_message = page.locator("[data-test='error']")

        assert error_message.is_visible()
        assert "locked out" in error_message.inner_text()
