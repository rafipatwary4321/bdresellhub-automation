from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = 'input[name="email"], input[type="email"]'
        self.password_input = 'input[name="password"], input[type="password"]'
        self.login_button = 'button[type="submit"], button:has-text("Login"), button:has-text("Sign In")'

    def load(self):
        self.page.goto("https://bdresellhub.com/login", wait_until="networkidle")

    def login(self, email, password):
        self.page.locator(self.email_input).first.fill(email)
        self.page.locator(self.password_input).first.fill(password)
        self.page.locator(self.login_button).first.click()