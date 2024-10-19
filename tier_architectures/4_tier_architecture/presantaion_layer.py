def display_menu():
    print("Welcome to the E-commerce Platform")
    print("Choose a number=> 1:View Products, 2:Add to Cart, 3:View Cart, 4:Checkout, 5:Exit")

def get_user_choice():
    return input("Pick a number from options: ")

def display_products(products):
    print("Available products")
    for idx, product in enumerate(products):
        print(f"{idx + 1}. {product['name']} - £{product['price']}")

def get_product_choice():
    return int(input("Enter the product number to add to cart: ")) - 1

def display_cart(cart):
    if not cart: print("Your cart is empty.")
    else:
       print("Your Cart:")
       for item in cart:
           print(f"{item['name']} - £{item['price']}")
def confirm_checkout():
    return input("Do you want to checkout? (yes/no): ").lower() == 'yes'