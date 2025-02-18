import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import Promotion, PercentDiscount, SecondHalfPrice, ThirdOneFree


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


def test_non_stocked_product():
    # Test the initialization of a NonStockedProduct instance
    product = NonStockedProduct("Windows License", 125)
    assert product.name == "Windows License"
    assert product.price == 125
    assert product.quantity == 0
    assert product.is_active() is True

    with pytest.raises(ValueError):
        product.set_quantity(10)  # Should raise an exception

    assert product.show() == "Windows License, Price: 125, Quantity: Not applicable"


def test_limited_product():
    # Test the initialization of a LimitedProduct instance
    product = LimitedProduct("Shipping", 10, 250, 1)
    assert product.name == "Shipping"
    assert product.price == 10
    assert product.quantity == 250
    assert product.maximum == 1
    assert product.is_active() is True

    with pytest.raises(ValueError):
        product.buy(2)  # Should raise an exception

    assert product.buy(1) == 10  # Should be allowed
    assert product.quantity == 249

    assert product.show() == "Shipping, Price: 10, Quantity: 249, Maximum per order: 1"


def test_percent_discount():
    product = Product("MacBook Air M2", 1450, 100)
    promotion = PercentDiscount("30% off!", 30)
    product.set_promotion(promotion)
    assert product.buy(1) == 1015  # 1450 * 0.7
    assert product.show() == "MacBook Air M2, Price: 1450, Quantity: 99, Promotion: 30% off!"

def test_second_half_price():
    product = Product("Bose QuietComfort Earbuds", 250, 500)
    promotion = SecondHalfPrice("Second Half price!")
    product.set_promotion(promotion)
    assert product.buy(2) == 375  # 250 + 125
    assert product.show() == "Bose QuietComfort Earbuds, Price: 250, Quantity: 498, Promotion: Second Half price!"

def test_third_one_free():
    product = Product("Google Pixel 7", 500, 250)
    promotion = ThirdOneFree("Third One Free!")
    product.set_promotion(promotion)
    assert product.buy(3) == 1000  # 500 * 2
    assert product.show() == "Google Pixel 7, Price: 500, Quantity: 247, Promotion: Third One Free!"

def test_remove_promotion():
    product = Product("MacBook Air M2", 1450, 100)
    promotion = PercentDiscount("30% off!", 30)
    product.set_promotion(promotion)
    product.set_promotion(None)  # Remove promotion
    assert product.buy(1) == 1450  # No discount applied
    assert product.show() == "MacBook Air M2, Price: 1450, Quantity: 99"
