import pytest

@pytest.mark.regression
def test_all_links_working(page):
    page.goto("https://bdresellhub.com/")

    links = page.locator("a")
    count = links.count()

    print(f"Total links: {count}")

    broken_links = []

    for i in range(count):
        href = links.nth(i).get_attribute("href")

        if href and href.startswith("http"):
            try:
                response = page.request.get(href)

                if response.status not in [200, 301, 302]:
                    broken_links.append((href, response.status))

            except:
                broken_links.append((href, "error"))

    assert len(broken_links) == 0, f"Broken links: {broken_links}"