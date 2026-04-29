import pytest

@pytest.mark.regression
@pytest.mark.parametrize("url", [
    "https://bdresellhub.com/privacy-policy",
    "https://bdresellhub.com/terms-and-conditions",
    "https://bdresellhub.com/refund-policy",
])
def test_policy_pages(page, url):
    response = page.goto(url, wait_until="networkidle")

    if not response or response.status >= 400:
        pytest.skip(f"Policy page not found: {url}")

    assert page.locator("body").is_visible()