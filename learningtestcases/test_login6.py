def test_login(page):

    page.goto("https://www.saucedemo.com/")

    assert page.title() == "Wrong Title"