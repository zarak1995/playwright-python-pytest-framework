
from pages.base_page import BasePage


class InventoryPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.product_title = ".title"
        self.add_to_cart_button = "#add-to-cart-sauce-labs-backpack"
        self.cart_badge = ".shopping_cart_badge"
        self.cart_link = ".shopping_cart_link"

    def get_product_title(self):

        return self.get_text(self.product_title)

    def add_product_to_cart(self):

        self.click(self.add_to_cart_button)

    def get_cart_count(self):

        return self.get_text(self.cart_badge)

    def open_cart(self):

        self.click(self.cart_link)
