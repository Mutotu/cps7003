class ECommercePlatform:
    def __init__(self, data_service):
        self.data_service = data_service
        self.cart = []

    def view_products(self):
        return self.data_service.get_products()

    def add_to_cart(self, product_index):
        product = self.data_service.get_products()[product_index]
        self.cart.append(product)

    def view_cart(self):
        return self.cart

    def checkout(self):
        total = sum(item['price'] for item in self.cart)
        order = {"items": self.cart, "total": total}
        self.data_service.save_order(order)
        self.cart = []
        return total


