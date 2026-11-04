
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # Enter credentials
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")

    # Click login
    page.locator("//input[@id='login-button']").click()

    # Explicit assertion wait
    expect(
        page.locator("//div[@class='inventory_list']")
    ).to_be_visible()

    print("Login successful!")

    browser.close()
