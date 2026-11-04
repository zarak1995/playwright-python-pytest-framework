
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_add_product_to_cart(page):

    # Login
    login_page = LoginPage(page)

    login_page.open_login_page()

    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    # Inventory page
    inventory_page = InventoryPage(page)

    assert inventory_page.get_product_title() == "Products"

    # Add product to cart
    inventory_page.add_product_to_cart()

    # Verify cart count
    assert inventory_page.get_cart_count() == "1"

    # Open cart
    inventory_page.open_cart()

    assert page.url.endswith("/cart.html")
