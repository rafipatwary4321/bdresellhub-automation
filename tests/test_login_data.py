import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.mark.parametrize("email,password", [
    ("test@example.com", "123456"),
    ("wrong@gmail.com", "wrongpass"),
    ("empty@test.com", "111111"),
])
def test_login_with_multiple_data(email, password):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.load()
        login_page.login(email, password)

        assert page.locator("body").is_visible()

        browser.close()