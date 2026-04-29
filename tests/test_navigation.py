from playwright.sync_api import sync_playwright

def test_navigation_pages():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/")
        assert page.locator("body").is_visible()

        browser.close()