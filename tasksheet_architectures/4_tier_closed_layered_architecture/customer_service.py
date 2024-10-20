# Business Logic Layer

class CustomerService:

    def __init__(self, data_service):
        self.data_service = data_service

    def get_customer_details(self, customer_id):
        return self.data_service.fetch_customer_details(customer_id)

    def get_customer_orders(self, customer_id):
        return  self.data_service.fetch_customer_orders(customer_id)
