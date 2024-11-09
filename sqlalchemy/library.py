from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select, ForeignKey

engine = create_engine('sqlite:///library.db', echo=False)
metadata = MetaData()
inspector = inspect(engine)

authors = Table('authors', metadata,
  Column('id', Integer, primary_key=True),
        Column('name', String))
books = Table('books', metadata,
  Column('id', Integer, primary_key=True),
        Column('title', String),
        Column('author_id', Integer, ForeignKey('authors.id')))

# metadata.create_all has to be called after the table creation
metadata.create_all(engine)

tables = inspector.get_table_names()

if "authors" in tables:
    print("Authors table exists")
else:
    print("Authors table doesn't exist")
if "authors" in tables:
    print("Books table exists")
else:
    print("Books table doesn't exist")

with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(authors.insert(), [
            {'name': 'J.K. Rowling'},
            {'name': 'J.R.R Tolkien'}
            ])
        trans.commit()
        print("\nData inserted successfully in table employees")
    except:
        trans.rollback()
        print("Transaction rolled back")

with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(books.insert(), [
            {'title': 'Harry Potter and the Philosopher\s Stone', 'author_id': 1},
            {'title': 'The Hobbit!', 'author_id': 2}
            ])
        trans.commit()
        print("\nData inserted successfully in table employees")
    except:
        trans.rollback()
        print("Transaction rolled back")

# Query the database
# Show content of 'authors' table
with engine.connect() as conn:
    result = conn.execute(select(authors))
    print("\nAuthors Table:")
    for row in result:
        print(row)
# Show content of 'books' table
with engine.connect() as conn:
    result = conn.execute(select(books))
    print("\nBooks Table:")
    for row in result:
        print(row)
# Show a book and its author
with engine.connect() as conn:
    result = conn.execute(select(books.c.title, authors.c.name).select_from(
    books.join(authors, books.c.author_id == authors.c.id)
        ))
    for row in result:
        print(f"\nBook: {row[0]}, Author: {row[1]}")