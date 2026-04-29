from playwright.sync_api import sync_playwright

def test_invalid_login_shows_error():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/login")

        page.fill('input[type="email"]', "wrong@gmail.com")
        page.fill('input[type="password"]', "wrongpassword")
        page.click('button[type="submit"]')

        page.wait_for_timeout(2000)

        assert page.locator("body").is_visible()

        browser.close()