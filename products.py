import promotions

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
        self.promotion = None  # Add promotion instance variable

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        promotion_info = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promotion_info}"

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