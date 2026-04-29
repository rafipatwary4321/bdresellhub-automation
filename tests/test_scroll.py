import pytest

@pytest.mark.regression
def test_scroll_page(page):
    page.goto("https://bdresellhub.com/")

    # Scroll down
    page.mouse.wheel(0, 3000)
    page.wait_for_timeout(1000)

    # Scroll up
    page.mouse.wheel(0, -3000)
    page.wait_for_timeout(1000)

    assert page.locator("body").is_visible()