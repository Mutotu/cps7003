import business_logic

def main():
    while True:
        print("1: Add Customer, 2: View Customer, 3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email:")
            business_logic.add_customer(name, email)
        elif choice == "2":
            customers = business_logic.get_customers()
            for customer in customers:
                print(f"ID: {customer[0]}, Name: {customer[1]}, Email: {customer[2]}")
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

