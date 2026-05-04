import time
import pytest

@pytest.mark.regression
def test_homepage_load_time(page):
    start = time.time()

    page.goto("https://bdresellhub.com/")
    page.wait_for_load_state("domcontentloaded")

    end = time.time()

    load_time = end - start
    print(f"Load time: {load_time:.2f} sec")

    assert load_time < 5