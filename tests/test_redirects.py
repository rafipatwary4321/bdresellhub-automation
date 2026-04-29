import pytest

@pytest.mark.regression
def test_login_link_redirect(page):
    page.goto("https://bdresellhub.com/")

    page.click("text=Sign In")

    page.wait_for_timeout(1000)

    assert "login" in page.url.lower()


@pytest.mark.regression
def test_signup_link_redirect(page):
    page.goto("https://bdresellhub.com/")

    page.click("text=Sign Up")

    page.wait_for_timeout(1000)

    assert "register" in page.url.lower() or "signup" in page.url.lower()