def test_faq_page(page):
    page.goto("https://bdresellhub.com/faq")

    assert page.locator("body").is_visible()

    faq_items = page.locator("button")

    if faq_items.count() > 0:
        faq_items.nth(0).click()