def test_navigation_pages(page):
    page.goto("https://bdresellhub.com/")
    assert page.locator("body").is_visible()

    page.goto("https://bdresellhub.com/pricing")
    assert page.locator("body").is_visible()

    page.goto("https://bdresellhub.com/faq")
    assert page.locator("body").is_visible()

    page.goto("https://bdresellhub.com/login")
    assert page.locator("body").is_visible()