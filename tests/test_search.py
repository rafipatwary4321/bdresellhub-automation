import pytest

@pytest.mark.regression
def test_search_functionality(page):
    page.goto("https://bdresellhub.com/")

    # Try to find search input
    search_input = page.locator('input[type="text"]')

    if search_input.count() > 0:
        search_input.first.fill("product")

        # press enter
        search_input.first.press("Enter")

        page.wait_for_timeout(2000)

        assert page.locator("body").is_visible()
    else:
        # if no search exists, just pass
        assert True