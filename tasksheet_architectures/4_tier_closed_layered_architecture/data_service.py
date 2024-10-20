# Data Services Layer

class DataService:

    def __init__(self, data_store):
        self.data_store = data_store

    def fetch_customer_details(self, customer_id):
        return self.data_store.load_customer_details(customer_id)

    def fetch_customer_orders(self, customer_id):
        return self.data_store.load_customer_orders(customer_id)
