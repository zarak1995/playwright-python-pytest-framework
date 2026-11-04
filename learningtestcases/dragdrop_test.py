
from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Create our own demo page
    page.set_content("""
    <html>
    <body>

        <h2>Playwright Drag and Drop Practice</h2>

        <div id="source"
             draggable="true"
             style="width:150px; padding:30px;
                    background:lightblue;">
            Drag Me
        </div>

        <br><br>

        <div id="target"
             style="width:250px; height:120px;
                    background:lightgray; padding:20px;">
            Drop Here
        </div>

        <script>

            const source = document.querySelector("#source");
            const target = document.querySelector("#target");

            source.addEventListener("dragstart", (event) => {
                event.dataTransfer.setData("text", "Drag Me");
            });

            target.addEventListener("dragover", (event) => {
                event.preventDefault();
            });

            target.addEventListener("drop", (event) => {
                event.preventDefault();

                target.innerText = "Dropped Successfully!";
                target.style.background = "lightgreen";
            });

        </script>

    </body>
    </html>
    """)

    # Locate elements
    source = page.locator("#source")
    target = page.locator("#target")

    # Verify elements
    assert source.is_visible()
    assert target.is_visible()

    print("Source and Target found!")

    # Perform Drag and Drop
    source.drag_to(target)

    # Verify result
    result = target.inner_text()

    print("Actual Result:", result)

    assert result == "Dropped Successfully!"

    print("PASS: Drag and Drop Successful!")

    page.wait_for_timeout(3000)

    browser.close()
