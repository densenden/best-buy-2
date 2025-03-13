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
                if product.promotion:
                    total_price += product.promotion.apply_promotion(product, quantity)
                else:
                    total_price += product.price * quantity
                if product.get_quantity() is not None:
                    product.set_quantity(product.get_quantity() - quantity)
            else:
                raise ValueError(f"Not enough stock for {product.name}")
        return total_price

    def place_order_form(self):
        """Allows a user to place an order by selecting products by number and entering quantities."""
        if not self.storage:
            print(Fore.RED + "The store is empty. No products available for order." + Style.RESET_ALL)
            return

        print(Fore.GREEN + "\nAvailable Products:" + Style.RESET_ALL)
        product_map = {}
        for index, product in enumerate(self.storage, start=1):
            product_map[str(index)] = product
            promotion_info = f", Promotion: {product.promotion.name}" if product.promotion else ""
            print(
                Fore.WHITE + f"{index}. {product.name}: {product.price}€ ({product.quantity} available){promotion_info}" + Style.RESET_ALL)

        shopping_list = []
        while True:
            product_number = input(
                Fore.WHITE + "\nEnter product number to order (or 'done' to finish): " + Style.RESET_ALL)

            if product_number.lower() == "done":
                break

            if product_number not in product_map:
                print(Fore.RED + "Invalid product number. Try again." + Style.RESET_ALL)
                continue

            product = product_map[product_number]

            try:
                quantity = int(input(Fore.WHITE + f"Enter quantity for {product.name}: " + Style.RESET_ALL))
                if quantity <= 0:
                    print(Fore.RED + "Quantity must be greater than 0." + Style.RESET_ALL)
                    continue
                if product.quantity is not None and quantity > product.quantity:
                    print(Fore.RED + f"Not enough stock. Only {product.quantity} available." + Style.RESET_ALL)
                    continue

                shopping_list.append((product, quantity))
                print(Fore.GREEN + f"Added {quantity}x {product.name} to cart." + Style.RESET_ALL)

            except ValueError:
                print(Fore.RED + "Invalid input. Please enter a number." + Style.RESET_ALL)

        if shopping_list:
            try:
                total_cost = self.order(shopping_list)
                print(Fore.GREEN + f"\nOrder placed successfully! Total cost: {total_cost}€" + Style.RESET_ALL)
            except ValueError as e:
                print(Fore.RED + str(e) + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "No products were ordered." + Style.RESET_ALL)

    def show_total_amount(self):
        total_quantity = self.get_total_quantity()
        total_value = sum(product.price * product.quantity for product in self.storage)
        print(Fore.YELLOW + "\nTotal amount in store:" + Style.RESET_ALL)
        print(Fore.WHITE + f"{total_quantity} items available" + Style.RESET_ALL)
        print(Fore.WHITE + f"Total store value: ${total_value}" + Style.RESET_ALL)