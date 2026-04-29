import pytest

@pytest.mark.regression
def test_login_empty_fields(page):
    page.goto("https://bdresellhub.com/login")

    # Click login without input
    page.click('button[type="submit"]')

    # Wait একটু
    page.wait_for_timeout(2000)

    # Check page still same (no redirect)
    assert "login" in page.url.lower()


@pytest.mark.regression
def test_login_invalid_credentials(page):
    page.goto("https://bdresellhub.com/login")

    page.fill('input[type="email"]', "wrong@test.com")
    page.fill('input[type="password"]', "wrongpass")

    page.click('button[type="submit"]')

    page.wait_for_timeout(2000)

    # Still on login page
    assert "login" in page.url.lower()