from config import Session
from base import create_tables
from models import Customer, Product, Order

# Create tables
create_tables()

# Start a session
session = Session()

# Add customers
customer1 = Customer(name='James Bond', email='bond@awl.com')
customer2 = Customer(name='Alicia Arnold', email='ali@yahoo.com')
customer3 = Customer(name = 'Jonny Stecchino', email = 'j.stec@virgilio.com')
customer4 = Customer(name = 'Brenda Willow', email = 'will@blue.com')
session.add_all([customer1, customer2, customer3, customer4])
session.commit()

# Add products
product1 = Product(name='Laptop', price=852.5)
product2 = Product(name='Smartphone', price=312.9)
product3 = Product(name = 'Headset', price = 25.3)
product4 = Product(name = 'Tablet', price = 150.0)
session.add_all([product1, product2, product3, product4])
session.commit()

# Create orders
order1 = Order(customer=customer1)
order1.products.append(product1)
order1.products.append(product2)
session.add(order1)
order2 = Order(customer=customer2)
order2.products.append(product3)
order2.products.append(product2)
session.add(order2)
order3 = Order(customer=customer3)
order3.products.append(product4)
session.add(order3)
order4 = Order(customer=customer4)
order4.products.append(product1)
order4.products.append(product2)
order4.products.append(product4)
session.add(order4)
session.commit()

# Query the database
for order in session.query(Order).all():
    print(f'Order {order.id} by {order.customer.name}:')
for product in order.products:
    print(f' - {product.name} at £{product.price}')
# Close the session
session.close()

# Query the database
for order in session.query(Order).all():
    print(f'Order {order.id} by {order.customer.name}:')
for product in order.products:
    print(f' - {product.name} at £{product.price}')
# Close the session
session.close()