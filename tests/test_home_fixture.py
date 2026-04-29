import pytest

@pytest.mark.smoke
def test_home_page_with_fixture(page):
    page.goto("https://bdresellhub.com/")
    assert page.locator("body").is_visible()