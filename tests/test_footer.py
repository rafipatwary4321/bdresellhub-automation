import pytest

@pytest.mark.regression
def test_footer_links(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    footer = page.locator("footer")

    if footer.count() > 0:
        links = footer.locator("a")
        assert links.count() > 0
    else:
        pytest.skip("Footer not found on page")