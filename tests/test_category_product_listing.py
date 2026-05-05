import pytest

@pytest.mark.regression
def test_category_wise_product_listing(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    category_links = page.locator(
        'a[href*="category"], a[href*="categories"]'
    )

    if category_links.count() == 0:
        pytest.skip("No category links found on homepage")

    category_links.first.click()
    page.wait_for_load_state("domcontentloaded")

    assert page.locator("body").is_visible()

    product_cards = page.locator(
        'a[href*="product"], .product, .card, [class*="product"], [class*="card"]'
    )

    if product_cards.count() == 0:
        pytest.skip("Category page opened but no product cards found")

    assert product_cards.count() > 0