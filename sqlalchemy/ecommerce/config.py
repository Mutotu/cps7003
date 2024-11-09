from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine and session
engine = create_engine('sqlite:///ecommerce.db', echo=False)
Session = sessionmaker(bind=engine)
