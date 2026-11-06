
import pytest
import pytest_html
import base64
import re

from pathlib import Path
from datetime import datetime


PROJECT_ROOT = Path(__file__).parent
SCREENSHOT_DIR = PROJECT_ROOT / "screenshots"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when in ("setup", "call") and report.failed:

        page = item.funcargs.get("page")

        if page is None:
            print("\nNo Playwright page available!")
            return

        try:
            if page.is_closed():
                print("\nPage is already closed!")
                return

            SCREENSHOT_DIR.mkdir(
                parents=True,
                exist_ok=True
            )

            safe_name = re.sub(
                r"[^a-zA-Z0-9_-]",
                "_",
                item.name
            )

            timestamp = datetime.now().strftime(
                "%Y%m%d_%H%M%S_%f"
            )

            screenshot_path = (
                SCREENSHOT_DIR /
                f"{safe_name}_{report.when}_{timestamp}.png"
            )

            # Capture screenshot
            page.screenshot(
                path=str(screenshot_path),
                full_page=True
            )

            print(f"\nScreenshot saved: {screenshot_path}")

            # Convert image bytes into Base64 string
            image_data = screenshot_path.read_bytes()

            base64_image = base64.b64encode(
                image_data
            ).decode("utf-8")

            # Attach screenshot to HTML report
            extras = getattr(report, "extras", [])

            extras.append(
                pytest_html.extras.image(
                    base64_image,
                    mime_type="image/png",
                    extension="png",
                    name="Failure Screenshot"
                )
            )

            report.extras = extras

            print("\nScreenshot attached to HTML report!")

        except Exception as e:
            print(f"\nScreenshot capture failed: {e}")



@pytest.fixture(scope="function", autouse=True)
def setup_test():

    print("\n========== Test Setup ==========")

    yield

    print("\n========== Test Teardown ==========")

