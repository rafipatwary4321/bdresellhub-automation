from playwright.sync_api import Page

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.name_input = 'input[name="name"], input[type="text"]'
        self.email_input = 'input[name="email"], input[type="email"]'
        self.password_input = 'input[name="password"], input[type="password"]'
        self.signup_button = 'button[type="submit"], button:has-text("Sign Up"), button:has-text("Register")'

    def load(self):
        self.page.goto("https://bdresellhub.com/register", wait_until="networkidle")

    def signup(self, name, email, password):
        self.page.locator(self.name_input).first.fill(name)
        self.page.locator(self.email_input).first.fill(email)
        self.page.locator(self.password_input).first.fill(password)
        self.page.locator(self.signup_button).first.click()