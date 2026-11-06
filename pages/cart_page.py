
from pages.base_page import BasePage


class CartPage(BasePage):

    def __init__(self, page):

        super().__init__(page)

        self.cart_product_name = ".cart_item .inventory_item_name"
        self.cart_quantity = ".cart_quantity"
        self.remove_button = "#remove-sauce-labs-backpack"
        self.continue_shopping_button = "#continue-shopping"

    def get_cart_product_name(self):

        return self.get_text(self.cart_product_name)

    def get_cart_quantity(self):

        return self.get_text(self.cart_quantity)

    def remove_product(self):

        self.click(self.remove_button)

    def continue_shopping(self):

        self.click(self.continue_shopping_button)

    def is_product_visible(self):
        return self.is_visible(self.cart_product_name)

    def checkout(self):
        self.click("#checkout")
