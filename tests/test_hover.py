import pytest

@pytest.mark.regression
def test_hover_elements(page):
    page.goto("https://bdresellhub.com/")

    elements = page.locator("a")

    if elements.count() > 0:
        elements.first.hover()
        page.wait_for_timeout(1000)

    assert page.locator("body").is_visible()