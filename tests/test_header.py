import pytest

@pytest.mark.regression
def test_header_navigation_visible(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    header_links = page.locator("header a, nav a")

    assert header_links.count() > 0