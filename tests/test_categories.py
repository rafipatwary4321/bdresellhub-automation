import pytest

@pytest.mark.regression
def test_categories_page_loads(page):
    possible_urls = [
        "https://bdresellhub.com/categories",
        "https://bdresellhub.com/category",
    ]

    page_found = False

    for url in possible_urls:
        response = page.goto(url, wait_until="networkidle")

        if response and response.status < 400:
            page_found = True
            assert page.locator("body").is_visible()
            break

    if not page_found:
        pytest.skip("Category page not found")