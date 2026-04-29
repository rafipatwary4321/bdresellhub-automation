from pages.login_page import LoginPage

def test_login_pom(page):
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("test@example.com", "123456")

    assert page.locator("body").is_visible()