import sqlite3

DB_NAME = 'database.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def get_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    return users
