from colorama import Fore, Style

class Store:

    def __init__(self, products=None):
        """Initializes the store with an optional list of products."""
        self.storage = products if products is not None else []

    def get_total_quantity(self):
        return sum(product.quantity for product in self.products)

    def quantity(self):
        return self.get_total_quantity()

    def add_product(self, product):
        """Adds a new product or increases quantity if it already exists."""
        for existing_product in self.storage:
            if existing_product.name == product.name:
                existing_product.quantity += product.quantity
                return
        self.storage.append(product)

    def remove_product(self, product):
        """Removes a product from store."""
        if product in self.storage:
            self.storage.remove(product)
        else:
            raise ValueError(f"Product '{product.name}' not found in store.")

    def get_total_quantity(self):  #-> int
        """Returns how many items are in the store in total."""
        return sum(product.quantity for product in self.storage)

    def get_all_products(self): # -> List[Product]
        """Returns all products in the store that are active."""
        return [product for product in self.storage if product.is_active()]

    def display_products(self):
        """Prints all products in a readable format, including current promotions."""
        print(Fore.GREEN + "\nAvailable Products:" + Style.RESET_ALL)
        for product in self.storage:
            promotion_info = f", Promotion: {product.promotion.name}" if product.promotion else ""
            print(
                Fore.WHITE + f"- {product.name}: {product.price}€ ({product.quantity} available){promotion_info}" + Style.RESET_ALL)

    def order(self, shopping_list):
        """Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order."""
        total_price = 0
        for product, quantity in shopping_list:
            if product in self.storage and (product.get_quantity() is None or product.get_quantity() >= quantity):
                total_price += product.buy(quantity)  # This line activates the buy method
                if product.get_quantity() is not None:
                    new_quantity = product.get_quantity() - quantity
                    if new_quantity < 0:
                        raise ValueError(f"Quantity cannot be negative for {product.name}")
                    product.set_quantity(new_quantity)
            else:
                raise ValueError(f"Not enough stock for {product.name}")
        return total_price

    def place_order_form(self):
        cart = []
        while True:
            print("\nAvailable Products:")
            for i, product in enumerate(self.storage, start=1):
                promotion = f", Promotion: {product.promotion.name}" if product.promotion else ""
                print(f"{i}. {product.name}: {product.price}€ ({product.quantity} available){promotion}")

            choice = input("Enter product number to order (or 'done' to finish): ")
            if choice.lower() == 'done':
                break

            try:
                product_index = int(choice) - 1
                if product_index < 0 or product_index >= len(self.storage):
                    print("Invalid product number.")
                    continue

                product = self.storage[product_index]
                quantity = int(input(f"Enter quantity for {product.name}: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue

                if product.quantity is not None and quantity > product.quantity:
                    print(f"Not enough stock. Only {product.quantity} available.")
                    continue

                cart.append((product, quantity))
                print(f"Added {quantity}x {product.name} to cart.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        if cart:
            total_cost = self.order(cart)
            print(f"Total order cost: {total_cost}€")
        else:
            print("No items in cart.")

    def show_total_amount(self):
        total_quantity = self.get_total_quantity()
        total_value = sum(product.price * product.quantity for product in self.storage)
        print(Fore.YELLOW + "\nTotal amount in store:" + Style.RESET_ALL)
        print(Fore.WHITE + f"{total_quantity} items available" + Style.RESET_ALL)
        print(Fore.WHITE + f"Total store value: ${total_value}" + Style.RESET_ALL)
