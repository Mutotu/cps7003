from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Create an engine that stores data in the local directory's library.db file
engine = create_engine('sqlite:///library.db', echo = False)
# Base class for your classes definitions
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
 # Relationship to the Book class
    books = relationship('Book', back_populates='author')



# Define the Book class
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))
 # Relationship to the Author class.
    author = relationship('Author', back_populates='books')



# Create tables if they do not exist
Base.metadata.create_all(engine)

# Add a new author
new_author = Author(name='George Orwell')
session.add(new_author)
session.commit()

# Add a new book
new_book = Book(title='1984', author=new_author)
session.add(new_book)
session.commit()


for book in session.query(Book).all():
    print(f'{book.title} by {book.author.name}')