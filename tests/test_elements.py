import pytest

@pytest.mark.regression
def test_multiple_elements_visible(page):
    page.goto("https://bdresellhub.com/")

    headers = page.locator("h1, h2, h3")
    buttons = page.locator("button")

    assert headers.count() > 0
    assert buttons.count() > 0