from playwright.sync_api import sync_playwright

def test_faq_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # FAQ page open
        page.goto("https://bdresellhub.com/faq")

        # Page load check
        assert page.locator("body").is_visible()

        # First FAQ item click
        faq_items = page.locator("button")

        if faq_items.count() > 0:
            faq_items.nth(0).click()

        browser.close()