class DataStore:
    def __init__(self):
        self.products = [
         {"name": "Laptop", "price": 999.99},
         {"name": "Smartphone", "price": 499.99},
         {"name": "Headphones", "price": 199.99}
        ]
        self.orders = []

    def load_products(self):
        return self.products

    def save_order(self, order):
        self.orders.append(order)