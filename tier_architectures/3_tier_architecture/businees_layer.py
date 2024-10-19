class BookingSystem:

    def __init__(self, data_store):
        self.data_store = data_store

    def book_room(self, name, room_type):
        booking = {'name': name, 'room_type': room_type}
        self.data_store.save_booking(booking)

    def get_all_bookings(self):
        return self.data_store.load_bookings()

    def cancel_booking(self, name):
        return self.data_store.cancel_booking(name)

    def modify_booking(self, name, room_type):
        booking = {'name': name, 'room_type': room_type}
        self.data_store.update_booking(booking)
