from playwright.sync_api import sync_playwright

def test_pricing_page_loads():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/pricing")

        assert page.locator("body").is_visible()
        assert "pricing" in page.url.lower()

        browser.close()