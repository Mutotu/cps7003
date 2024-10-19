#####   Application is divided into 2 layers    ####
# Client tier => presentation layer where the user interface resides
# Server tier  the data layer where the database and data processing logic are located
# Client tier runs on  the client machine and responsible for displaying data to the user and collecting user input
# Server tier runs on  a server ad responsible for storing, retrieving, and managing data
# The way the client communicates with the server => Directly => client sends requests to the server, and the server processes these requests and sends back the appropriate responses
# Database is stored on the server
#  Interface installed on the client is used to access the database
##############
# In a 2-tier architecture, you typically have a client (user interface) and a server (database) layer.
# A basic example is that of a user (client tier) interacting with a SQL database (server tier)
##############
# Write two simple python codes for:
# Client (User Interface) Layer: it connects to the SQLite database and queries it about the user’s tasks stored in it
# Server (Database) Layer: it sets up the SQLite database and creates a table if it does not exist that contains a list of tasks that the user is to do

# Client Layer
#       Client (User Interface) Layer: it connects to the SQLite database and queries the database about all the tasks stored in the database
#       This is the front-end part of the system where users interact with the application
#       The database is named “user-tasks”
#       The table is named “tasks”
#       This layer queries the table to get all the tasks listed in it and their priorities
#       The tasks and their priorities are printed as a table with headings: “Nb” (this is the task id), “Task” (name of the task), and “Priority” (priority of the task)



import sqlite3

def create_table(conn):
    """Create the tasks table if it doesn't exist"""
    try:
        sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        priority integer
                                    );"""
        conn.execute(sql_create_tasks_table)
        print("Table 'tasks' created successfully.")
    except sqlite3.Error as e:
        print(e)

def insert_sample_tasks(conn):
    tasks = [
        ('Task 1', 1),
        ('Task 2', 2),
        ('Task 3', 3)
    ]
    cur = conn.cursor()
    cur.executemany("INSERT INTO tasks (name, priority) VALUES (?, ?)", tasks)
    conn.commit()

def create_connection(db_file):
    """create a database connection to the SQLite database"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}")
    except sqlite3.Error as e:
        print(e)
    return conn

def query_all_tasks(conn):
    """Query all the rows in the tasks table"""
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")

    rows = cur.fetchall()
    for row in rows:
        print(row)


def main():
    database = "user-tasks.db"

    # create a database connection
    conn = create_connection(database)
    insert_sample_tasks(conn)
    with conn:
        # Create the table if it doesn't exist
        create_table(conn)

        # Insert data or query tasks
        print("Tasks and their priorities are: ")
        print("{:<5} {:<30} {:<10}".format("nb", "task", "priority"))
        query_all_tasks(conn)


def select_all_tasks(conn):
    cur = conn.cursor()
    cur.execute("SELECT id, name, priority from tasks")
    rows = cur.fetchall()
    for row in rows:
        print("{:<5} {:<30} {:<10}".format(row[0], row[1], row[2]))


if __name__ == "__main__":
    main()





