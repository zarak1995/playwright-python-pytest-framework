from playwright.sync_api import sync_playwright, expect

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://the-internet.herokuapp.com/iframe")

    frame = page.frame_locator("#mce_0_ifr")

    editor = frame.locator("body#tinymce")

    editor.click()
    editor.fill("Learning Playwright iFrames!")

    expect(editor).to_contain_text("Learning Playwright iFrames!")

    print("iFrame interaction successful!")

    browser.close()