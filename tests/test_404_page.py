import pytest

@pytest.mark.regression
def test_404_page_for_invalid_route(page):
    response = page.goto("https://bdresellhub.com/this-page-does-not-exist")
    page.wait_for_load_state("domcontentloaded")

    assert response.status in [404, 500]
    assert page.locator("body").is_visible()

    print(f"Invalid route status: {response.status}")