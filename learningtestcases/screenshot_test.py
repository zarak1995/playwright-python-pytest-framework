
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # 1. Normal screenshot
    page.screenshot(path="normal.png")

    # 2. Full page screenshot
    page.screenshot(
        path="full_page.png",
        full_page=True
    )

    # 3. Element screenshot
    page.locator("#login-button").screenshot(
        path="login_button.png"
    )

    print("All screenshots captured successfully!")

    browser.close()
