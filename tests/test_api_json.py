import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_api_json_validation():
    with sync_playwright() as p:
        request = p.request.new_context()

        response = request.get("https://bdresellhub.com/")

        assert response.status == 200

        content_type = response.headers.get("content-type", "")

        if "application/json" in content_type:
            data = response.json()
            assert data is not None
        else:
            pytest.skip("Homepage is not JSON API response")

        request.dispose()