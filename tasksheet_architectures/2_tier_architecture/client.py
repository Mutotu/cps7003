import sqlite3
from random import randint


def create_connection(db_file):
    """create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def add_book(conn, book):
    """add a new book to the books table"""
    sql = '''INSERT INTO books(title, author, year) VALUES(?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()
    return cur.lastrowid

def view_books(conn):
    """query and display all the books"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def main():
    database = "library.db"
    #  create a database connection
    conn = create_connection(database)
    if conn is not None:
        while True:
            print("1: Add book, 2: View Books, 3: Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                year = input("Enter book year: ")
                add_book(conn, (title, author, year))
            elif choice == "2":
                view_books(conn)
            elif choice == "3":
                break
            else: print("Invalid choice")
    else:
        print("Error! cannot create a database communication")

if __name__ == "__main__":
    main()