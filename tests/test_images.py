from playwright.sync_api import sync_playwright

def test_images_are_loaded():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://bdresellhub.com/")

        images = page.locator("img")
        count = images.count()

        print(f"Total images: {count}")

        for i in range(count):
            src = images.nth(i).get_attribute("src")

            if src:
                response = page.request.get(src)
                assert response.status == 200

        browser.close()