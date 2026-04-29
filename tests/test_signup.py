from playwright.sync_api import sync_playwright

def test_signup_page_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/register")

        assert page.locator("body").is_visible()

        # Try common input fields
        inputs = page.locator("input")
        print(f"Total inputs found: {inputs.count()}")

        browser.close()