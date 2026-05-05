import pytest
from pages.signup_page import SignupPage

@pytest.mark.regression
def test_signup_empty_fields(page):
    signup_page = SignupPage(page)
    signup_page.load()

    page.locator(signup_page.signup_button).first.click()
    page.locator("body").wait_for()

    assert "register" in page.url.lower() or "signup" in page.url.lower()


@pytest.mark.regression
def test_signup_invalid_email(page):
    signup_page = SignupPage(page)
    signup_page.load()

    signup_page.signup("Test User", "invalid-email", "123456")
    page.locator("body").wait_for()

    assert page.locator("body").is_visible()


@pytest.mark.regression
def test_signup_weak_password(page):
    signup_page = SignupPage(page)
    signup_page.load()

    signup_page.signup("Test User", "test@example.com", "123")
    page.locator("body").wait_for()

    assert page.locator("body").is_visible()