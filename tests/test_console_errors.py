def test_home_page_has_no_console_errors(page):
    console_errors = []

    def handle_console(msg):
        if msg.type == "error":
            console_errors.append(msg.text)

    page.on("console", handle_console)

    page.goto("https://bdresellhub.com/", wait_until="networkidle")

    assert len(console_errors) == 0, f"Console errors found: {console_errors}"