
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.username = "#user-name"
        self.password = "#password"
        self.login_button = "#login-button"
        self.error_message = "[data-test='error']"

    def open_login_page(self):

        self.navigate("https://www.saucedemo.com/")

    def login(self, username, password):

        self.fill(self.username, username)
        self.fill(self.password, password)
        self.click(self.login_button)

    def get_error_message(self):

        return self.get_text(self.error_message)
