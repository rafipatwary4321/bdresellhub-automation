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

    assert page_found, "No contact/support/help page found"