import pytest

@pytest.mark.regression
def test_product_details_page(page):
    page.goto("https://bdresellhub.com/")  # REMOVE networkidle

    page.wait_for_load_state("domcontentloaded")

    items = page.locator("a")

    if items.count() > 0:
        first_item = items.first
        href = first_item.get_attribute("href")

        if href and href.startswith("http"):
            first_item.click()

            page.wait_for_load_state("domcontentloaded")

            assert page.locator("body").is_visible()
        else:
            pytest.skip("No valid product link found")
    else:
        pytest.skip("No clickable items found")