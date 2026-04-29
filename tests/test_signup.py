import pytest
from pages.signup_page import SignupPage

@pytest.mark.regression
def test_signup_page_form(page):
    signup_page = SignupPage(page)
    signup_page.load()

    assert page.locator("body").is_visible()