import pytest

@pytest.mark.regression
def test_https_and_no_mixed_content(page):
    mixed_content_errors = []

    def handle_console(msg):
        text = msg.text.lower()
        if "mixed content" in text:
            mixed_content_errors.append(msg.text)

    page.on("console", handle_console)

    response = page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    assert response.status == 200
    assert page.url.startswith("https://")
    assert len(mixed_content_errors) == 0, f"Mixed content errors found: {mixed_content_errors}"