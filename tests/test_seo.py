import pytest

@pytest.mark.regression
def test_basic_seo_elements(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    # Title check
    title = page.title()
    assert title is not None and len(title) > 0

    # Meta description
    meta_desc = page.locator('meta[name="description"]').get_attribute("content")
    assert meta_desc is not None

    # Canonical link (optional)
    canonical = page.locator('link[rel="canonical"]')

    if canonical.count() > 0:
        href = canonical.first.get_attribute("href")
        assert href is not None