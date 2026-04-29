from playwright.sync_api import sync_playwright

def test_home_page_has_no_console_errors():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        console_errors = []

        page.on("console", lambda msg: console_errors.append(msg.text) if msg.type == "error" else None)

        page.goto("https://bdresellhub.com/", wait_until="networkidle")

        browser.close()

        assert len(console_errors) == 0, f"Console errors found: {console_errors}"