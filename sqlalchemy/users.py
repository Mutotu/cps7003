from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select

engine = create_engine('sqlite:///users.db', echo=False)
metadata = MetaData()
inspector = inspect(engine)

tables = inspector.get_table_names()
users = Table('users', metadata,
  Column('id', Integer, primary_key=True),
        Column('full_name', String),
        Column('age', Integer),
        Column('city', String))

# metadata.create_all has to be called after the table creation
metadata.create_all(engine)

if "users" in tables:
    print("Users table exists")
else:
    print("Users table doesn't exist")
with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(users.insert(), [
            {'full_name': 'Jonathan Pommel', 'age': 30, 'city':'London'},
            {'full_name': 'Amanda Elliot', 'age': 25, 'city': 'Hull'},
            {'full_name': 'James Brown', 'age': 55, 'city': 'Durham'},
            ])
        trans.commit()
        print("\nData inserted successfully in table employees")
    except:
        trans.rollback()
        print("Transaction rolled back")


print("Ran insert method")

with engine.connect() as connection:
    stmt = select(users)
    result = connection.execute(stmt)
    rows = result.fetchall()
    print("\nTable users':")
    for row in rows:
        print(row)

print("Ran select ")