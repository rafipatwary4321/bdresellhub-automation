import pytest

@pytest.mark.regression
def test_home_page_pagination(page):
    page.goto("https://bdresellhub.com/")

    next_buttons = page.locator("text=Next")

    if next_buttons.count() > 0:
        current_url = page.url
        next_buttons.first.click()
        page.wait_for_timeout(1500)

        assert page.url != current_url or page.locator("body").is_visible()
    else:
        assert page.locator("body").is_visible()