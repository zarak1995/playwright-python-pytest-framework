from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto("https://www.saucedemo.com/")

        page.locator("#wrong-id").click(timeout=2000)

        print("Login button clicked")

    except TimeoutError:
        print("Timeout error occurred")

    finally:
        print("Closing browser")
        browser.close()