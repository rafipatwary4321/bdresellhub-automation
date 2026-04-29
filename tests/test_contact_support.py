
import pytest

@pytest.mark.regression
def test_contact_or_support_page(page):
    possible_urls = [
        "https://bdresellhub.com/contact",
        "https://bdresellhub.com/support",
        "https://bdresellhub.com/help",
    ]

    page_found = False

    for url in possible_urls:
        response = page.goto(url, wait_until="networkidle")

        if response and response.status < 400:
            page_found = True
            assert page.locator("body").is_visible()
            break

    if not page_found:
        pytest.skip("No contact/support/help page found on website")