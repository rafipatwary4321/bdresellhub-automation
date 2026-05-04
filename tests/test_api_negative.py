import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.regression
def test_login_api():
    with sync_playwright() as p:
        request = p.request.new_context()

        payload = {
            "email": "wrong@test.com",
            "password": "wrongpass"
        }

        response = request.post(
            "https://bdresellhub.com/api/login",  # ← change if needed
            data=payload
        )

        print(response.status)
        print(response.text())

        assert response.status in [200, 400, 401]

        request.dispose()