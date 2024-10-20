import sqlite3

def create_connection():
    conn = sqlite3.connect('crm.db')
    return conn

def add_customer(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()

def get_customers():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return customers