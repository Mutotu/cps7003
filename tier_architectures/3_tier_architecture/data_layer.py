class DataStore:

    def __init__(self):
        self.bookings = []

    def save_booking(self, booking):
        self.bookings.append(booking)

    def load_bookings(self):
        return self.bookings

    def cancel_booking(self, name):
        for booking in self.bookings:
            if booking["name"] == name:
                self.bookings.remove(booking)
                return
        print("User not found")
        return

    def update_booking(self, booking):
        name = booking['name']
        room_type = booking['room_type']
        for booking in self.bookings:
            if booking["name"] == name:
                booking["room_type"] = room_type
                return
        print("User not found")
        return