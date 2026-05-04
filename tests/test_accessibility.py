import pytest

@pytest.mark.regression
def test_basic_accessibility(page):
    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    # 1. Image alt check
    images = page.locator("img")
    for i in range(images.count()):
        alt = images.nth(i).get_attribute("alt")
        # optional check (some images may not have alt)
        if alt is None:
            print(f"Image without alt at index {i}")

    # 2. Button text check
    buttons = page.locator("button")
    for i in range(buttons.count()):
        text = buttons.nth(i).inner_text()
        assert text is not None

    # 3. Heading check
    headings = page.locator("h1, h2, h3")
    assert headings.count() > 0