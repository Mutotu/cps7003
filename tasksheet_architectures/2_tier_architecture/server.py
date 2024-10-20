import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """Create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except Error as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table for storing books"""
    try:
        sql_create_books_table = """CREATE TABLE IF NOT EXISTS books(
        id integer PRIMARY KEY,
        title text NOT NULL,
        author text NOT NULL,
        year integer
        );"""
        conn.execute(sql_create_books_table)
    except Error as e:
        print(e)

def main():
    database = "library.db"
    # create a database connection
    con = create_connection(database)

    # create tables
    if con is not None:
        create_table(con)
    else:
        print("Error! cannot create the database connection")

if __name__ == "__main__":
    main()