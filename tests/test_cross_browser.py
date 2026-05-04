import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
@pytest.mark.parametrize("browser_name", ["chromium", "firefox", "webkit"])
def test_homepage_cross_browser(browser_name):
    with sync_playwright() as p:
        browser = getattr(p, browser_name).launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/")
        page.wait_for_load_state("domcontentloaded")

        assert page.locator("body").is_visible()

        browser.close()