import sqlite3
from sqlite3 import Error
import os

def create_connection(db_file):
    """ create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    """ create a table from the create_table_sql statement """
    try:
        sql_create_tasks_table = """ CREATE TABLE IF NOT EXISTS tasks (
        id integer PRIMARY KEY,
        name text NOT NULL,
        priority integer
        ); """
        conn.execute(sql_create_tasks_table)
    except Error as e:
        print(e)
def insert_task(conn, task):
    """ insert a new task into the tasks table """
    sql = ''' INSERT INTO tasks(name, priority)
    VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid


def main():
    os.remove("user-tasks.db")
    database = "user-tasks.db"
 # create a database connection
    conn = create_connection(database)
  # create tables
    if conn is not None:
        create_table(conn)
 # insert user's tasks with different priorities with 1 being the heighest priority and 3 the least
        tasks = [
    ('Complete project report', 1),
    ('Prepare presentation', 2),
    ('Attend team meeting', 3),
    ('Review code', 2),
    ('Plan next sprint', 1)
        ]
        for task in tasks:
            insert_task(conn, task)
        print("Sample data inserted successfully.")
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    main()