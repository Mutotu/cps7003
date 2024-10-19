
from data_layer import  DataStore
from data_service_layer import DataService
from business_layer import ECommercePlatform
from presantaion_layer import display_products, display_menu, display_cart, get_product_choice, get_user_choice, confirm_checkout

def main():
    data_store = DataStore()
    data_service = DataService(data_store)
    ecommerce_platform = ECommercePlatform(data_service)


    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            products = ecommerce_platform.view_products()
            display_products(products)

        elif choice == '2':
            products = ecommerce_platform.view_products()
            display_products(products)
            product_index = get_product_choice()
            ecommerce_platform.add_to_cart(product_index)
            print("Product added to cart!")
        elif choice == '3':
            cart = ecommerce_platform.view_cart()
            display_cart(cart)
        elif choice == '4':
            cart = ecommerce_platform.view_cart()
            display_cart(cart)
            if confirm_checkout():
                total = ecommerce_platform.checkout()
                print(f"Checkout successful! Total amount: £{total}")
            else:
                print("Checkout cancelled.")

        elif choice == '5':
            print("Exiting the platform. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()