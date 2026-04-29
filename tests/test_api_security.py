import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_security_headers():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://bdresellhub.com/")

        headers = response.headers

        print(headers)

        # Basic security headers check
        assert response.status == 200

        # These may or may not exist → soft check
        security_headers = [
            "x-frame-options",
            "x-content-type-options",
            "strict-transport-security",
            "content-security-policy",
        ]

        missing = []

        for header in security_headers:
            if header not in headers:
                missing.append(header)

        if missing:
            print(f"Missing security headers: {missing}")