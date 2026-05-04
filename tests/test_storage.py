import pytest

@pytest.mark.regression
def test_browser_storage_after_homepage_load(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    cookies = page.context.cookies()
    local_storage_count = page.evaluate("window.localStorage.length")
    session_storage_count = page.evaluate("window.sessionStorage.length")

    print(f"Cookies: {len(cookies)}")
    print(f"LocalStorage items: {local_storage_count}")
    print(f"SessionStorage items: {session_storage_count}")

    assert page.locator("body").is_visible()