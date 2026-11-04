def test_login(page):
    page.goto("https://www.saucedemo.com/")

    assert page.title() == "Swag Labs"

    print("Login page opened successfully!")