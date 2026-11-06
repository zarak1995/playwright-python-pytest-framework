
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_remove_product_from_cart(page):

    # Login
    login = LoginPage(page)
    login.open_login_page()
    login.login("standard_user", "secret_sauce")

    # Add product
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()

    # Open cart
    inventory.open_cart()

    # Initialize CartPage
    cart = CartPage(page)

    # Verify product exists
    assert cart.is_product_visible() == True

    # Remove product
    cart.remove_product()

    # Verify product removed
    assert cart.is_product_visible() == False
