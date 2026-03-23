from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
    @property
    def heading(self):
        return self.page.get_by_role("heading", name="Login")

    @property
    def username_input(self):
        return self.page.locator('[name="username"]')

    @property
    def password_input(self):
        return self.page.locator('[name="password"]')

    @property
    def login_button(self):
        return self.page.get_by_role("button", name="Login")

    @property
    def error_message(self):
        return self.page.get_by_text("Invalid", exact=False)

    # Actions
    def goto(self, base_url):
        self.page.goto(f"{base_url}")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
