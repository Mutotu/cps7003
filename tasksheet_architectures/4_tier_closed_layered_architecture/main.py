from data_store import DataStore
from data_service import DataService
from customer_service import CustomerService
from presentation_layer import display_customer_orders, display_customer_details, display_menu, get_customer_id, get_user_choice

def main():
    data_store = DataStore()
    data_service = DataService(data_store)
    customer_service = CustomerService(data_service)
    while True:
        display_menu()
        choice = get_user_choice()
        if choice == '1':
            customer_id = get_customer_id()
            details = customer_service.get_customer_details(customer_id)
            display_customer_details(details)
        elif choice == '2':
            customer_id = get_customer_id()
            orders = customer_service.get_customer_orders(customer_id)
            display_customer_orders(orders)
        elif choice == '3':
            print("Exiting the platform. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
 main()