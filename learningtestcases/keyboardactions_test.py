
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create demo webpage
    page.set_content("""
    <html>
    <body>
        <h2>Playwright Mouse & Keyboard Practice</h2>

        <input id="username" placeholder="Enter username">

        <br><br>

        <button id="double">Double Click Me</button>

        <p id="double_result">Double clicks: 0</p>

        <button id="right">Right Click Me</button>

        <p id="right_result">Right click not performed</p>

        <br><br>

        <div id="menu" style="padding:20px; background:lightblue;">
            Hover Over Me
            <div id="submenu" style="display:none;">
                Dropdown Menu Visible!
            </div>
        </div>

        <script>
            let count = 0;

            document.querySelector("#double")
                .addEventListener("dblclick", () => {
                    count++;
                    document.querySelector("#double_result")
                        .innerText = "Double clicks: " + count;
                });

            document.querySelector("#right")
                .addEventListener("contextmenu", (e) => {
                    e.preventDefault();
                    document.querySelector("#right_result")
                        .innerText = "Right click performed";
                });

            document.querySelector("#menu")
                .addEventListener("mouseenter", () => {
                    document.querySelector("#submenu")
                        .style.display = "block";
                });
        </script>
    </body>
    </html>
    """)

    # 1. FILL
    username = page.locator("#username")
    username.fill("admin")
    print("Username filled")

    # 2. PRESS - Control + A
    username.press("Control+A")
    print("Existing text selected")

    # 3. KEYBOARD.TYPE
    page.keyboard.type("Playwright User")
    print("New text typed")

    # 4. PRESS - Backspace
    username.press("End")
    username.press("Backspace")
    print("Backspace pressed")

    # 5. PRESS - Enter
    username.press("Enter")
    print("Enter pressed")

    # 6. MOUSE HOVER
    page.locator("#menu").hover()
    print("Mouse hover performed")

    assert page.locator("#submenu").is_visible()

    # 7. DOUBLE CLICK
    page.locator("#double").dblclick()
    print("Double click performed")

    assert page.locator("#double_result").inner_text() == "Double clicks: 1"

    # 8. RIGHT CLICK
    page.locator("#right").click(button="right")
    print("Right click performed")

    assert page.locator("#right_result").inner_text() == "Right click performed"

    # Final verification
    print("All Mouse and Keyboard Actions completed successfully!")

    page.wait_for_timeout(3000)

    browser.close()
