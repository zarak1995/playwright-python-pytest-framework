
from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # Login
    page.locator("//input[@id='user-name']").fill("standard_user")
    page.locator("//input[@id='password']").fill("secret_sauce")
    page.locator("//input[@id='login-button']").click()

    # Assertion 1: Simple Python assertion
    assert "inventory" in page.url

    # Assertion 2: Playwright assertion
    expect(page).to_have_title("Swag Labs")

    # Assertion 3: Element visibility
    expect(
        page.locator("//div[@class='inventory_list']")
    ).to_be_visible()

    # Assertion 4: Verify products count
    expect(
        page.locator("//div[@class='inventory_item']")
    ).to_have_count(6)

    print("All assertions passed!")

    browser.close()
