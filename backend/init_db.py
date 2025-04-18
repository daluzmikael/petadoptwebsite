# init_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Create users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Create pets table
    c.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            owner_id INTEGER,
            FOREIGN KEY(owner_id) REFERENCES users(id)
        )
    ''')

    # Create extra table
    c.execute('''
        CREATE TABLE IF NOT EXISTS extra (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            info TEXT NOT NULL
        )
    ''')

    # List of Users
    users = [
        ('alice', 'alice@example.com'),
        ('bob', 'bob@example.com'),
        ('carol', 'carol@example.com'),
        ('dave', 'dave@example.com'),
        ('eve', 'eve@example.com'),
        ('frank', 'frank@example.com'),
        ('grace', 'grace@example.com'),
        ('heidi', 'heidi@example.com')
    ]
    c.executemany("INSERT OR IGNORE INTO users (username, email) VALUES (?, ?)", users)

    # List of Pets
    pets = [
        ('Fluffy', 'Cat', 1),
        ('Rover', 'Dog', 2),
        ('Goldie', 'Fish', 3),
        ('Spike', 'Hedgehog', 4),
        ('Mittens', 'Cat', 5),
        ('Buddy', 'Dog', 6),
        ('Charlie', 'Parrot', 7),
        ('Daisy', 'Rabbit', 8),
        ('Luna', 'Cat', 1),
        ('Rocky', 'Dog', 2),
        ('Bubbles', 'Fish', 3),
        ('Nibbles', 'Hamster', 4),
    ]
    c.executemany("INSERT INTO pets (name, species, owner_id) VALUES (?, ?, ?)", pets)

    #  extra data
    c.execute("INSERT OR IGNORE INTO extra (id, info) VALUES (?, ?)", (1, "Welcome to the extended API!"))

    conn.commit()
    conn.close()
    print("Database initialized with extended sample data.")

if __name__ == "__main__":
    init_db()
