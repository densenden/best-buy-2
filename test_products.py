import pytest
from products import Product


def test_product_initialization():
    # Test the initialization of a Product instance
    product = Product("MacBook Air M2", 1450, 100)
    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.quantity == 100
    assert product.active is True

    with pytest.raises(Exception):
        Product("", 1450, 100)  # Name cannot be empty
    with pytest.raises(Exception):
        Product("MacBook", -100, 10)  # Price cannot be negative
    with pytest.raises(Exception):
        Product("MacBook", 100, -10)  # Quantity cannot be negative


def test_get_quantity():
    # Test the get_quantity method
    product = Product("Bose QuietComfort Earbuds", 250, 500)
    assert product.get_quantity() == 500


def test_set_quantity():
    # Test the set_quantity method
    product = Product("Bose QuietComfort Earbuds", 250, 500)
    product.set_quantity(200)
    assert product.quantity == 200

    product.set_quantity(0)
    assert product.is_active() is False  # Should be deactivated


def test_is_active():
    # Test the is_active method
    product = Product("MacBook Air M2", 1450, 100)
    assert product.is_active() is True
    product.deactivate()
    assert product.is_active() is False
    product.activate()
    assert product.is_active() is True


def test_activate_deactivate():
    # Test the activate and deactivate methods
    product = Product("MacBook Air M2", 1450, 100)
    product.deactivate()
    assert product.active is False
    product.activate()
    assert product.active is True


def test_show():
    # Test the show method
    product = Product("MacBook Air M2", 1450, 100)
    assert product.show() == "MacBook Air M2, Price: 1450, Quantity: 100"


def test_buy():
    # Test the buy method
    product = Product("MacBook Air M2", 1450, 100)
    assert product.buy(10) == 14500  # 10 * 1450
    assert product.quantity == 90  # 100 - 10

    with pytest.raises(Exception):
        product.buy(200)  # Buying more than available should raise an exception

    product.buy(90)  # Buy all remaining quantity
    assert product.quantity == 0
    assert product.is_active() is False  # Product should be deactivated


