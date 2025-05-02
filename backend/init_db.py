# init_db.py
import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("PRAGMA foreign_keys = ON;")

    # Users
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Pets
    c.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            owner_id INTEGER,
            FOREIGN KEY(owner_id) REFERENCES users(id)
        )
    ''')

    # Events
    c.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            date TEXT NOT NULL
        )
    ''')

    # RSVPed events
    c.execute('''
        CREATE TABLE IF NOT EXISTS rsvped_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            event_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(event_id) REFERENCES events(id)
        )
    ''')

    # Saved pets
    c.execute('''
        CREATE TABLE IF NOT EXISTS saved_pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            pet_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(pet_id) REFERENCES pets(id)
        )
    ''')

    # Extra info table
    c.execute('''
        CREATE TABLE IF NOT EXISTS extra (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            info TEXT NOT NULL
        )
    ''')

    # Sample users
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

    # Sample pets
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
    c.executemany("INSERT OR IGNORE INTO pets (name, species, owner_id) VALUES (?, ?, ?)", pets)

    # Sample events
    events = [
        ("Adopt-a-thon Weekend", "2025-05-04"),
        ("Puppy Yoga", "2025-05-10"),
        ("Summer Cat Café Meetup", "2025-05-15")
    ]
    c.executemany("INSERT OR IGNORE INTO events (id, name, date) VALUES (?, ?, ?)", [(i+1, e[0], e[1]) for i, e in enumerate(events)])

    # Extra info
    c.execute("INSERT OR IGNORE INTO extra (id, info) VALUES (?, ?)", (1, "Welcome to the extended API!"))

    conn.commit()
    conn.close()
    print("Database initialized with sample users, pets, and events.")

if __name__ == "__main__":
    init_db()
