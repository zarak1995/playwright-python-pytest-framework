from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/windows")

    print("Parent tab:", page.title())

    with page.expect_popup() as popup_info:
        page.get_by_text("Click Here").click()

    new_page = popup_info.value

    print("New tab:", new_page.title())

    expect(new_page.locator("h3")).to_have_text("New Window")

    print("New tab interaction successful!")

    new_page.close()

    print("New tab closed")

    browser.close()