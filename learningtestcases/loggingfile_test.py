import logging
from playwright.sync_api import sync_playwright, expect

logging.basicConfig(
    filename="automation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        logging.info("Browser launched")

        page.goto("https://www.saucedemo.com/")
        logging.info("SauceDemo website opened")

        page.locator("#user-name").fill("standard_user")
        page.locator("#password").fill("secret_sauce")

        logging.info("Username and password entered")

        page.locator("#login-button").click()
        logging.info("Login button clicked")

        expect(page.locator(".title")).to_have_text("Products")

        logging.info("Login successful - Test Passed")

    except Exception:
        logging.exception("Test failed")
        raise

    finally:
        browser.close()
        logging.info("Browser closed")