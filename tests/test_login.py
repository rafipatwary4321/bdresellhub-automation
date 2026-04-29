from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.load()
        login_page.login("test@example.com", "123456")

        browser.close()