import sqlite3

def create_connection():
    conn = sqlite3.connect('crm.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT NOT NULL,
                            email TEXT NOT NULL
                        )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_table()