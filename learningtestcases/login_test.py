
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    # Launch browser
    browser = p.chromium.launch(headless=False)

    # Create page
    page = browser.new_page()

    # Open website
    page.goto("https://www.saucedemo.com/")

    # Enter username using XPath
    page.locator("//input[@id='user-name']").fill("standard_user")

    # Enter password using XPath
    page.locator("//input[@id='password']").fill("secret_sauce")

    # Click login button using XPath
    page.locator("//input[@id='login-button']").click()

    # Print current URL
    print("Current URL:", page.url)

    # Close browser
    browser.close()
