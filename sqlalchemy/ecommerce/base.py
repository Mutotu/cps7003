from sqlalchemy.orm import declarative_base
from config import engine

# Base class for ORM models
Base = declarative_base()

# Function to create tables
def create_tables():
    Base.metadata.create_all(engine)
