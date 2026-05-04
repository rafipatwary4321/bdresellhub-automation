import pytest

@pytest.mark.regression
@pytest.mark.parametrize("width,height,device", [
    (1920, 1080, "desktop"),
    (768, 1024, "tablet"),
    (390, 844, "mobile"),
])
def test_homepage_responsive(page, width, height, device):
    page.set_viewport_size({"width": width, "height": height})

    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    assert page.locator("body").is_visible()

    print(f"Responsive test passed for {device}")