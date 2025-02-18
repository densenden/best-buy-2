import pytest
from store import Store
from products import Product


def test_add_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    best_buy = Store([bose])
    best_buy.add_product(mac)
    assert mac in best_buy.storage


def test_remove_product():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    best_buy = Store([bose])
    best_buy.remove_product(bose)
    assert bose not in best_buy.storage


def test_get_total_quantity():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    best_buy = Store([bose, mac])
    assert best_buy.get_total_quantity() == 600


def test_get_all_products():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    pixel = Product("Google Pixel 7", price=500, quantity=250)
    best_buy = Store([bose, mac, pixel])
    pixel.set_quantity(0)  # Set Pixel to inactive
    active_products = best_buy.get_all_products()
    assert len(active_products) == 2
    assert pixel not in active_products


def test_order():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)
    best_buy = Store([bose, mac])
    total_price = best_buy.order([(bose, 5), (mac, 30)])
    assert total_price == (5 * 250) + (30 * 1450)  # 1250 + 43500 = 44750
    assert bose.get_quantity() == 495  # 500 - 5
    assert mac.get_quantity() == 70  # 100 - 30


def test_order_insufficient_stock():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=2)
    best_buy = Store([bose])
    with pytest.raises(ValueError, match="Not enough stock for Bose QuietComfort Earbuds"):
        best_buy.order([(bose, 5)])


if __name__ == "__main__":
    pytest.main()
