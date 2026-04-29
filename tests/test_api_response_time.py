import time
import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_homepage_response_time():
    with sync_playwright() as p:
        request = p.request.new_context()

        start_time = time.time()
        response = request.get("https://bdresellhub.com/")
        end_time = time.time()

        response_time = end_time - start_time

        print(f"Response time: {response_time:.2f} seconds")

        assert response.status == 200
        assert response_time < 5

        request.dispose()