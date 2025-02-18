from abc import ABC, abstractmethod

class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass

class PercentDiscount(Promotion):
    def __init__(self, name, percent):
        super().__init__(name)
        self.percent = percent / 100

    def apply_promotion(self, product, quantity):
        return round(product.price * quantity * (1 - self.percent))

class SecondHalfPrice(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_items = quantity // 2 + quantity % 2
        half_price_items = quantity // 2
        return product.price * full_price_items + (product.price * half_price_items * 0.5)

class ThirdOneFree(Promotion):
    def apply_promotion(self, product, quantity):
        full_price_items = quantity - (quantity // 3)
        return product.price * full_price_items