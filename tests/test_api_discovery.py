import pytest

@pytest.mark.regression
def test_api_endpoint_discovery_from_network(page):
    discovered_urls = []

    def capture_request(request):
        url = request.url
        if "/api/" in url or "graphql" in url or "ajax" in url:
            discovered_urls.append(url)

    page.on("request", capture_request)

    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    print("Discovered API endpoints:")
    for url in discovered_urls:
        print(url)

    assert page.locator("body").is_visible()