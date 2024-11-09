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

# Add a new user to the table
# new_user = User(name='Alice', age=30)
# session.add(new_user)
# session.commit()

l = [ User(name='Alice1', age=30), User(name='Alice2', age=30), User(name='Alice3', age=30)]
for user in l:
    session.add(user)
session.commit()
# Query the table
for user in session.query(User).all():
    print(user.name, user.age)

# Close the session
session.close()
