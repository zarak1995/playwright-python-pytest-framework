from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto("https://www.saucedemo.com/")

        page.locator("#wrong-button").click(timeout=3000)

    except TimeoutError:
        print("Element not found within 3 seconds")

    finally:
        browser.close()