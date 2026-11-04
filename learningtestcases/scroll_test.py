
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create demo page
    page.set_content("""
    <html>
    <body style="height:2000px">

        <h1>Playwright Scrolling Practice</h1>

        <div style="margin-top:1200px">
            <button id="submit">Submit Button</button>
        </div>

    </body>
    </html>
    """)

    # 1. Mouse wheel scrolling
    page.mouse.wheel(0, 500)
    page.wait_for_timeout(1000)

    print("Mouse scroll completed")

    # 2. Scroll to specific element
    page.locator("#submit").scroll_into_view_if_needed()
    page.wait_for_timeout(1000)

    print("Scrolled to Submit button")

    # 3. Verify visibility
    assert page.locator("#submit").is_visible()

    # 4. Scroll to top
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(1000)

    print("Scrolled to top")

    # 5. Scroll to bottom
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(1000)

    print("Scrolled to bottom")

    print("PASS: All scrolling operations completed!")

    browser.close()
