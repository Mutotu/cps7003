# Data Store Layer

class DataStore:

    def __init__(self):
        self.customers = {
        "1": {"id": "1", "name": "Ollie Smith", "email": "ollie@gmail.com"},
        "2": {"id": "2", "name": "Luke Chamberlain", "email": "l.chamberlain@yahoo.com"},
        "3": {"id": "3", "name": "Luke2 Chamberlain2", "email": "2l.chamberlain@yahoo.com"}
        }
        self.orders = {
        "1": [{"id": "564", "total": 150.75}, {"id": "560", "total": 200.50}],
        "2": [{"id": "12", "total": 99.99}],
         "3": []
        }

    def load_customer_details(self, customer_id):
        return self.customers.get(customer_id)

    def load_customer_orders(self, customer_id):
        return self.orders.get(customer_id)