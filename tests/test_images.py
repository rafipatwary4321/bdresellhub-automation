def test_images_are_loaded(page):
    page.goto("https://bdresellhub.com/")

    images = page.locator("img")
    count = images.count()

    print(f"Total images: {count}")

    broken_images = []

    for i in range(count):
        src = images.nth(i).get_attribute("src")

        if src and src.startswith("http"):
            response = page.request.get(src)

            if response.status not in [200, 403]:
                broken_images.append(src)

    assert len(broken_images) == 0, f"Broken images found: {broken_images}"