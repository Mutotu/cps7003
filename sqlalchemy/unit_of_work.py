from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database URL
DATABASE_URL = 'sqlite:///example.db'

# Create an engine
engine = create_engine(DATABASE_URL, echo=True)

# Define a base class for declarative class definitions
Base = declarative_base()

# Define a User class that represents the users table
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the users table in the database
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
session = Session()

# Start a transaction
try:
    # Add a new user
    new_user = User(name='Alice', age=30)
    session.add(new_user)

    # Update an existing user
    existing_user = session.query(User).filter_by(name='Bob').first()
    if existing_user:
        existing_user.age = 35
# Commit the transaction
    session.commit()
except:
    # Rollback the transaction in case of error
    session.rollback()
    raise
finally:
    # Close the session
    session.close()