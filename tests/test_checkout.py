
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(page):

    # Step 1: Login
    login = LoginPage(page)
    login.open_login_page()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory = InventoryPage(page)
    inventory.add_product_to_cart()

    # Step 3: Open cart
    inventory.open_cart()

    # Step 4: Checkout
    cart = CartPage(page)
    cart.checkout()

    # Step 5: Enter customer information
    checkout = CheckoutPage(page)

    checkout.enter_customer_information(
        "Zarak",
        "Shah",
        "75500"
    )

    # Step 6: Continue to overview
    checkout.continue_checkout()

    # Step 7: Finish order
    checkout.finish_checkout()

    # Step 8: Verify confirmation
    assert checkout.get_confirmation_message() == "Thank you for your order!"
