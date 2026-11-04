def test_login(page):
    page.goto("https://www.saucedemo.com/")

    print("Page title:", page.title())

    print("URL:", page.url)

    assert page.title() == "Swag Labs"