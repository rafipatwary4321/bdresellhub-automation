import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_homepage_response_headers():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://bdresellhub.com/")

        headers = response.headers

        print(headers)

        assert response.status == 200
        assert "content-type" in headers

        request.dispose()