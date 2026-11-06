
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_cart_product(page):

    # Initialize LoginPage
    login = LoginPage(page)

    # Open website FIRST
    login.open_login_page()

    # Login
    login.login("standard_user", "secret_sauce")

    # Add product to cart
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()

    # Open cart
    inventory.open_cart()

    # Cart page
    cart = CartPage(page)

    # Verify product name
    assert cart.get_cart_product_name() == "Sauce Labs Backpack"

    # Verify quantity
    assert cart.get_cart_quantity() == "1"
