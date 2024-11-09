# Python DBAPI

import sqlite3
# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('user.db')
# Create a cursor object to interact with the database
cursor = conn.cursor()
# Create a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        job TEXT
        )
            ''')

# Insert data
cursor.execute('''
INSERT INTO users (name, age, job) VALUES (?, ?, ?)
''', ('Alexandra Hamilton', 50, 'data analyst'))
cursor.execute('''
INSERT INTO users (name, age, job) VALUES (?, ?, ?)
''', ('Mark Hanson', 65, 'cybersecurity consultant'))
cursor.execute('''
INSERT INTO users (name, age, job) VALUES (?, ?, ?)
''', ('Monica Geller', 31, 'software engineer'))
cursor.execute('''
INSERT INTO users (name, age, job) VALUES (?, ?, ?)
''', ('Sheldon Cooper', 27, 'computing modeler'))
# Commit the changes
conn.commit()


# Query the database
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
# Print the results
for row in rows:
    print(row)
# Close the connection
conn.close()