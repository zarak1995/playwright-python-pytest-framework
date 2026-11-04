from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.locator("#wrong-id").click(timeout=2000)

    except TimeoutError:
        print("Timeout exception")

    except Exception as e:
        print("General exception:", e)

    finally:
        print("Test completed")