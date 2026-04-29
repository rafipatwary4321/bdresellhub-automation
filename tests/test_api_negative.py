import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_invalid_api_route_returns_error_status():
    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.get("https://bdresellhub.com/invalid-test-route-404")

        assert response.status in [404, 403]

        request.dispose()