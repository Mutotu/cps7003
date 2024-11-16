from datetime import date
from sqlalchemy import create_engine, Column, Integer, String, Float, and_, or_, Date
from sqlalchemy.orm import declarative_base, sessionmaker


# Create an engine that stores data in the local directory's university.db file
engine = create_engine('sqlite:///car_dealer_database.db')
# Base class for our classes definitions.
Base = declarative_base()


class Car(Base):
    __tablename__ = 'cars'

    id = Column(Integer, primary_key=True)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    mileage = Column(Integer, nullable=False)
    date_added = Column(Date, nullable=False)



# Create all tables in the engine
Base.metadata.create_all(engine)
# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

session.add_all([Car(make="Toyota", model="Camry", year=2018, price=18000, mileage=31000, date_added=date(2023, 1, 15)),
                 Car(make="Honda", model="Civic", year=2019, price=195000, mileage=22000, date_added=date(2023, 2, 20)),
                 Car(make="Ford", model="Focus", year=2017, price=15000, mileage=45000, date_added=date(2023, 3, 10)),
                 Car(make="Renault", model="Clio", year=2021, price=25000, mileage=10000, date_added=date(2024, 6, 10)),
                 Car(make="Skoda", model="Octavia", year=2020, price=21500, mileage=18000, date_added=date(2024, 9, 23)),
                    ])
session.commit()

toyota_cars = session.query(Car).filter(Car.make == 'Toyota', Car.year > 2015, Car.price < 20000).all()
# Print the results
print("Toyota cars manufactured after 2015 with price less than £20000")
for car in toyota_cars:
  print(f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Price: £{car.price}")

# Complex Filtering with AND/OR Conditions
# Cars that are either Toyota or Honda and priced below 20000 or have mileage below 50000
filtered_cars = session.query(Car).filter(
    or_(Car.make == 'Toyota',Car.make == 'Honda'),
            and_(Car.price < 20000,Car.mileage < 50000)).all()

print("\nToyota or Honda cars with price less than £20000 and mileage below 50000")
for car in filtered_cars:
 print( f"ID: {car.id}, Make: {car.make}, Model: {car.model}, Year: {car.year}, Price: £{car.price}, Mileage: {car.mileage}")