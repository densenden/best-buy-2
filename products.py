class Product:

    def __init__(self, name, price, quantity):
        if not name:
            raise ValueError("Enter a name. This can't be empty.")

        if price < 0:
            raise ValueError("Price cannot be negative.")

        if quantity < 0:
            raise ValueError("Quantity Error: What were you thinking?")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):  # -> float
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("We cannot handle negative stock.")

        self.quantity = quantity

        self.active = quantity > 0

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):  # -> str
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity): # -> float
        # enough there?
        if quantity > self.quantity:
            raise ValueError(f"We do not have enough {self.name} in stock. Please order maximum {self.quantity} {self.name}")
        if quantity < 0:
            raise ValueError("We cannot handle negative orders.")
        if quantity == self.quantity:
            self.active = False

        self.quantity = self.quantity - quantity

        return int(self.price * quantity)


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