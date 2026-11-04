def test_login(page, setup_test):

    page.goto("https://www.saucedemo.com/")

    assert page.title() == "Swag Labs"