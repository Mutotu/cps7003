class DataService:
    def __init__(self, data_store):
        self.data_store = data_store

    def get_products(self):
        return self.data_store.load_products()

    def save_order(self, order):
        self.data_store.save_order(order)