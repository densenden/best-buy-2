import promotions

class Product:
    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Enter a name. This can't be empty.")
        self._name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Add promotion instance variable

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity Error: What were you thinking?")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __str__(self):
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} Quantity:{self.quantity}{promotion_info}"

    def buy(self, quantity):
        if quantity > self.quantity:
            raise ValueError(f"We do not have enough {self.name} in stock. Please order maximum {self.quantity} {self.name}")
        if quantity < 0:
            raise ValueError("You cannot buy a negative quantity of a product.")
        if quantity == self.quantity:
            self.active = False
        self.quantity -= quantity
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price > other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity):
        raise ValueError("Cannot set quantity for non-stocked products.")

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: Not applicable"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity):
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} of {self.name} in one order.")
        return super().buy(quantity)

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, Maximum per order: {self.maximum}"