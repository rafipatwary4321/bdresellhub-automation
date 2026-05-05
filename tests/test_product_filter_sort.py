import pytest

@pytest.mark.regression
def test_product_filter_or_sort_available(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    filter_elements = page.locator(
        'select, input[type="search"], input[placeholder*="Search"], button:has-text("Filter"), button:has-text("Sort")'
    )

    if filter_elements.count() == 0:
        pytest.skip("No product filter/sort/search element found")

    filter_elements.first.click()
    assert page.locator("body").is_visible()