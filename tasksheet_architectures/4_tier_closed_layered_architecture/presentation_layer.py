def display_menu():
    print("E-commerce Platform - Customer Information Retrieval")
    print("1. View Customer Details")
    print("2. View Customer Orders")
    print("3. Exit")

def get_user_choice():
    return input("Enter your choice: ")

def get_customer_id():
    return input("Enter customer ID: ")

def display_customer_details(details):
    if details:
        print(f"Customer ID: {details['id']}")
        print(f"Name: {details['name']}")
        print(f"Email: {details['email']}")
    else:
        print("Customer not found.")

def display_customer_orders(orders):
    if orders:
        print("Customer Orders:")
        for order in orders:
            print(f"Order ID: {order['id']}, Total: £{order['total']}")
    else:
        print("No orders found for this customer.")