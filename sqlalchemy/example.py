from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, inspect, select

engine = create_engine('sqlite:///example.db', echo=False)
metadata = MetaData()
inspector = inspect(engine)

employees = Table('employees', metadata,
  Column('id', Integer, primary_key=True),
        Column('first_name', String),
        Column('last_name', String))

# metadata.create_all has to be called after the table creation
metadata.create_all(engine)
tables = inspector.get_table_names()
print("Ran table class")

if "employees" in tables:
    print("Employees table exists")
else:
    print("Employee table doesn't exist")
with engine.connect() as connection:
    trans = connection.begin()
    try:
        connection.execute(employees.insert(), [
            {'first_name': 'Alex', 'last_name': 'Graham'},
            {'first_name': 'Bobby', 'last_name': 'Bowl'}
            ])
        trans.commit()
        print("\nData inserted successfully in table employees")
    except:
        trans.rollback()
        print("Transaction rolled back")


print("Ran insert method")

with engine.connect() as connection:
    stmt = select(employees)
    result = connection.execute(stmt)
    rows = result.fetchall()
    print("\nTable employees':")
    for row in rows:
        print(row)

print("Ran select ")