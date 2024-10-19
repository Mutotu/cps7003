def display_menu():
    print("Welcome to the Hotel Booking System")
    print("Options=> 1:Book a Room, 2:View Bookings, 3: Cancel a booking, 4: Modify a booking 5:Exit")

def get_user_choice():
    return input("Enter a choice number: ")

def get_user_details():
    name = input("Enter your name: ")
    room_type = input("Enter single or double: ")
    return name, room_type

def cancel_booking():
    return input("Enter name to cancel your booking: ")

def display_bookings(bookings):
    if not bookings: print("No bookings found!")
    else:
        for booking in bookings:
            print(f"Name: {booking['name']}, Room Type: {booking['room_type']}")

def modify_booking():
    name = input("Enter name to modify your room: ")
    room_type = input("Enter new type for room: ")
    return name, room_type