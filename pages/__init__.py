from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = 'input[type="email"]'
        self.password_input = 'input[type="password"]'
        self.login_button = 'button[type="submit"]'

    def load(self):
        self.page.goto("https://bdresellhub.com/login")

    def login(self, email, password):
        self.page.fill(self.email_input, email)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)