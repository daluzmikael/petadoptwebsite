import sqlite3

def create_connection():
    conn = sqlite3.connect("backend/app.db")
    return conn

def initialize_database():
    conn = create_connection()
    cursor = conn.cursor()

    # Example: Create a 'pets' table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        species TEXT NOT NULL,
        breed TEXT,
        age INTEGER
    );
    """)

    # cursor.execute("INSERT INTO pets (name, species, breed, age) VALUES (?, ?, ?, ?)", ("Buddy", "Dog",    "Lab", 3))

    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    initialize_database()
