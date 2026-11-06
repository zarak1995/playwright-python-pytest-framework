
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.first_name = "#first-name"
        self.last_name = "#last-name"
        self.postal_code = "#postal-code"
        self.continue_button = "#continue"
        self.finish_button = "#finish"
        self.complete_message = ".complete-header"

    def enter_customer_information(self, first_name, last_name, postal_code):

        self.fill(self.first_name, first_name)
        self.fill(self.last_name, last_name)
        self.fill(self.postal_code, postal_code)

    def continue_checkout(self):

        self.click(self.continue_button)

    def finish_checkout(self):

        self.click(self.finish_button)

    def get_confirmation_message(self):

        return self.get_text(self.complete_message)
