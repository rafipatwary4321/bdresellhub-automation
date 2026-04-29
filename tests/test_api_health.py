import pytest
from playwright.sync_api import APIRequestContext, sync_playwright

@pytest.mark.regression
def test_homepage_api_status():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://bdresellhub.com/")

        assert response.status == 200

        request.dispose()