from marshmallow.fields import Float
from sqlalchemy import Column, Integer, String, ForeignKey, Table, Float
from sqlalchemy.orm import relationship
from base import Base

# Define association table for many-to-many relationships
order_product_table = Table(
    'order_products', Base.metadata,
    Column('customer_id', Integer, ForeignKey('orders.id')),
          Column('product_id', Integer, ForeignKey('products.id')),
)

# Define the Customer class
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # Many-to-many relationships
    orders = relationship('Order', back_populates='customer')

# Define the Product class
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    orders = relationship('Order', secondary=order_product_table, back_populates='products')

# Define the Order class
class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
     # Relationship to the Customer class
    customer = relationship('Customer', back_populates='orders')
     # Relationship to the Product class through the order_product_table
    products = relationship('Product', secondary=order_product_table, back_populates='orders')