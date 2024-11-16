from datetime import datetime, date
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, func, case
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Create an engine and a session
engine = create_engine('sqlite:///car_dealer_database_expanded.db')
Session = sessionmaker(bind=engine)
session = Session()
# Defining a Model
Base = declarative_base()
# Define the Car class to map to the cars table
class Car(Base):

    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    price = Column(Integer)
    mileage = Column(Integer)
    date_added = Column(Date)
    sales = relationship('Sale', back_populates='car') # one-to-many relationship with the Sale class, indicating that one car can have multiple sales

class Salesperson(Base):
    __tablename__ = 'salespersons'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    sales = relationship('Sale', back_populates='salesperson')

# Define the Sale class to map to the sales table
class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'))
    salesperson_id = Column(Integer, ForeignKey('salespersons.id'))
    sale_date = Column(Date)
    sale_price = Column(Integer)

    car = relationship('Car', back_populates='sales') # many-to-one relationship with the Car class
    salesperson = relationship('Salesperson', back_populates='sales') # many-to-one relationship with the Salesperson class. Each Sale is associated with one Car and one Salesperson
# Create the tables
Base.metadata.create_all(engine)

# Add records to table cars
Toyota = Car(make='Toyota', model='Camry', year=2018, price=18000, mileage=31000, date_added=date(2023, 1, 15))
Honda = Car(make='Honda', model='Civic', year=2019, price=19500, mileage=22000, date_added=date(2023, 2, 20))
Ford = Car(make='Ford', model='Focus', year=2017, price=15000, mileage=45000, date_added=date(2023, 3, 10))
Renault = Car(make='Renault', model='Clio', year=2021, price=25000, mileage=10000, date_added=date(2024, 6, 10))
Skoda = Car(make='Skoda', model='Octavia', year=2020, price=21500, mileage=18000, date_added=date(2024, 9, 23))

Callum = Salesperson(name='Callum Jones')
Malcom = Salesperson(name='Malcom Brenner')
Jennifer = Salesperson(name='Jennifer Finnegan')
Martin = Salesperson(name='Martin Yates')

session.add_all([Toyota, Honda, Ford, Renault, Skoda, Callum, Malcom, Jennifer, Martin])
session.commit()

# Add records to sales table
sale1 = Sale(car_id=Toyota.id, salesperson_id=Callum.id, sale_date=date(2023, 4, 5), sale_price=17500)
sale2 = Sale(car_id=Honda.id, salesperson_id=Malcom.id, sale_date=date(2023, 5, 10), sale_price=19000)
sale3 = Sale(car_id=Ford.id, salesperson_id=Jennifer.id, sale_date=date(2024, 3, 30), sale_price=36500)
sale4 = Sale(car_id=Renault.id, salesperson_id=Martin.id, sale_date=date(2024, 5, 28), sale_price=65200)
sale5 = Sale(car_id=Skoda.id, salesperson_id=Malcom.id, sale_date=date(2024, 7, 5), sale_price=41000)
sale6 = Sale(car_id=Toyota.id, salesperson_id=Jennifer.id, sale_date=date(2024, 8, 30), sale_price=23800)
sale7 = Sale(car_id=Ford.id, salesperson_id=Callum.id, sale_date=date(2024, 9, 2), sale_price=31300)
sale8 = Sale(car_id=Ford.id, salesperson_id=Martin.id, sale_date=date(2024, 9, 18), sale_price=41200)
# Add sales to the session and commit
session.add_all([sale1, sale2, sale3, sale4, sale5, sale6, sale7, sale8])
session.commit()

# Print tables
cars = session.query(Car).all()
print("\nCars:")
for car in cars:
    print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Price: {car.price}, Mileage: {car.mileage}, Date Added: {car.date_added}")

salespersons = session.query(Salesperson).all()
print("\nSalespersons:")
for salesperson in salespersons:
    print(f"ID: {salesperson.id}, Name: {salesperson.name}")

sales = session.query(Sale).all()
print("\nSales:")
for sale in sales:
    print(f"Car ID: {sale.car_id}, Salesperson ID: {sale.salesperson_id}, Sale date: {sale.sale_date}, Sale price: {sale.sale_price}")