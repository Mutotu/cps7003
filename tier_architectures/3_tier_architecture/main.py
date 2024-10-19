from data_layer import DataStore
from businees_layer import BookingSystem
from presentation_layer import display_menu, get_user_choice, get_user_details, display_bookings, cancel_booking, modify_booking


def main():
    data_store = DataStore()
    booking_system = BookingSystem(data_store)

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            name, room_type = get_user_details()
            booking_system.book_room(name, room_type)
            print(f"Room booked successfully for {name}")
        elif choice == "2":
            bookings = booking_system.get_all_bookings()
            display_bookings(bookings)
        elif choice == "3":
            name = cancel_booking()
            booking_system.cancel_booking(name)
        elif choice == "4":
            name, room_type = modify_booking()
            booking_system.modify_booking(name, room_type)
            print(f"Room for {name} modified")
        elif choice == "5":
            print("Exiting the system")
            break
        else: print("Invalid choice. Try again")

if __name__ =="__main__":
    main()