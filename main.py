from colorama import Fore, Style
from products import Product
from store import Store
import products
import promotions

def store_demo():
    """Creates instances, simulates a budget-conscious shopping experience, and adds some Aldi-flavor."""
    print(Fore.YELLOW + "Stocking Aldi shelves with top-tier budget products..." + Style.RESET_ALL)

    baguette = Product("Aldi's 39-cent Baguette", price=0.39, quantity=1000)
    cheese = Product("Aldi’s 1-Euro Mystery Cheese", price=1.00, quantity=500)
    toilet_paper = Product("Aldi XXL Toilet Paper Pack (Because You Never Know)", price=3.99, quantity=200)

    aldi_sued = Store([baguette, cheese])
    print(Fore.WHITE + f"Initial total quantity in Aldi Süd: {aldi_sued.get_total_quantity()}" + Style.RESET_ALL)

    print(
        Fore.YELLOW + "A budget-conscious customer demands more deals... adding the legendary toilet paper!" + Style.RESET_ALL)
    aldi_sued.add_product(toilet_paper)
    print(
        Fore.WHITE + f"Total quantity after adding toilet paper: {aldi_sued.get_total_quantity()}" + Style.RESET_ALL)

    print(
        Fore.YELLOW + "A customer finds out the cheese is actually goat cheese... returning it!" + Style.RESET_ALL)
    aldi_sued.remove_product(cheese)
    print(
        Fore.WHITE + f"Total quantity after removing the cheese: {aldi_sued.get_total_quantity()}" + Style.RESET_ALL)

    print(
        Fore.YELLOW + "Placing a very strategic order: 10 baguettes and 2 toilet paper packs (classic combo)." + Style.RESET_ALL)
    order_cost = aldi_sued.order([(baguette, 10), (toilet_paper, 2)])
    print(
        Fore.WHITE + f"Total order cost (including the typical Aldi surprise discount): {order_cost}" + Style.RESET_ALL)

    print(
        Fore.YELLOW + "Checking remaining products in store... what’s left after the morning rush?" + Style.RESET_ALL)
    active_products = aldi_sued.get_all_products()
    for product in active_products:
        print(Fore.WHITE + f"- {product.name}: {product.quantity} available" + Style.RESET_ALL)

    print(Fore.YELLOW + "Final total quantity in Aldi Süd:" + Style.RESET_ALL)
    print(Fore.WHITE + f"{aldi_sued.quantity()}" + Style.RESET_ALL)

    print(
        Fore.GREEN + "Remember: If it's not in stock, come back next week – maybe it'll be back, maybe it'll be gone forever!" + Style.RESET_ALL)


def quit_store():
    print(Fore.YELLOW + "\nExiting store management. Goodbye!" + Style.RESET_ALL)
    exit()


def start(store):
    user_selection = {
        "1": store.display_products,
        "2": store.show_total_amount,
        "3": store.place_order_form,
        "4": store_demo,
        "5": quit_store
    }

    while True:
        print(Fore.YELLOW + "\n==================================" + Style.RESET_ALL)
        print(Fore.YELLOW + "        STORE MANAGEMENT" + Style.RESET_ALL)
        print(Fore.YELLOW + "==================================\n" + Style.RESET_ALL)
        print(Fore.YELLOW + " 1   2   3   4   5 " + Style.RESET_ALL)
        print(Fore.YELLOW + "-------------------" + Style.RESET_ALL)
        print(Fore.WHITE + " 1 - LIST ALL PRODUCTS" + Style.RESET_ALL)
        print(Fore.WHITE + " 2 - SHOW TOTAL AMOUNT" + Style.RESET_ALL)
        print(Fore.WHITE + " 3 - MAKE AN ORDER" + Style.RESET_ALL)
        print(Fore.WHITE + " 4 - SHOW STORE DEMO" + Style.RESET_ALL)
        print(Fore.WHITE + " 5 - QUIT" + Style.RESET_ALL)
        print(Fore.YELLOW + "==================================\n" + Style.RESET_ALL)

        choice = input(Fore.WHITE + "Enter your choice: " + Style.RESET_ALL)

        if choice in user_selection:
            result = user_selection[choice]()
            if result is not None:
                print(Fore.GREEN + str(result) + Style.RESET_ALL)
        else:
            print(Fore.RED + "\nInvalid choice, please select a valid option." + Style.RESET_ALL)


def main():
    """Instantiation of product, store and menu."""
    # setup initial stock of inventory
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    products.NonStockedProduct("Windows License", price=125),
                    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)

    best_buy = Store(product_list)

    # Show that menu.
    start(best_buy)





if __name__ == "__main__":
    main()