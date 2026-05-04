import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page(request):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.set_default_timeout(10000)

        yield page

        if request.node.rep_call.failed:
            screenshot_path = f"reports/{request.node.name}.png"
            page.screenshot(path=screenshot_path, full_page=True)

        browser.close()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)