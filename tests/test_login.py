from playwright.sync_api import sync_playwright

def test_login_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/login")

        # input email
        page.fill('input[type="email"]', "test@example.com")

        # input password
        page.fill('input[type="password"]', "123456")

        # click login
        page.click('button[type="submit"]')

        browser.close()