import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("PRAGMA foreign_keys = ON;")

    # Users table with password
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Pets table with new fields
    c.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            species TEXT NOT NULL,
            breed TEXT NOT NULL,
            age INTEGER NOT NULL,
            allergen TEXT NOT NULL,
            temperament TEXT NOT NULL,
            owner_id INTEGER,
            FOREIGN KEY(owner_id) REFERENCES users(id)
        )
    ''')

    # Saved pets
    c.execute('''
        CREATE TABLE IF NOT EXISTS saved_pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            pet_id INTEGER,
            UNIQUE(user_id, pet_id),
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(pet_id) REFERENCES pets(id)
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
            UNIQUE(user_id, event_id),
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(event_id) REFERENCES events(id)
        )
    ''')

    # Extra info table
    c.execute('''
        CREATE TABLE IF NOT EXISTS extra (
            id INTEGER PRIMARY KEY,
            info TEXT NOT NULL
        )
    ''')

    # Sample users with password
    users = [
        ('alice', 'alice@example.com', 'password123'),
        ('bob', 'bob@example.com', 'password123'),
        ('carol', 'carol@example.com', 'password123'),
        ('dave', 'dave@example.com', 'password123'),
        ('eve', 'eve@example.com', 'password123'),
        ('frank', 'frank@example.com', 'password123'),
        ('grace', 'grace@example.com', 'password123'),
        ('heidi', 'heidi@example.com', 'password123')
    ]
    c.executemany("INSERT OR IGNORE INTO users (username, email, password) VALUES (?, ?, ?)", users)

    # Sample pets (with full fields)
    pets = [
        ('Fluffy', 'Cat', 'Siamese', 2, 'None', 'Playful', 1),
        ('Rover', 'Dog', 'Labrador', 4, 'None', 'Friendly', 2),
        ('Goldie', 'Fish', 'Goldfish', 1, 'None', 'Calm', 3),
        ('Spike', 'Hedgehog', 'African Pygmy', 3, 'None', 'Quiet', 4),
        ('Mittens', 'Cat', 'Tabby', 5, 'None', 'Curious', 5),
        ('Buddy', 'Dog', 'Beagle', 6, 'None', 'Energetic', 6),
        ('Charlie', 'Parrot', 'Macaw', 3, 'Feathers', 'Talkative', 7),
        ('Daisy', 'Rabbit', 'Dutch', 2, 'Hay', 'Gentle', 8),
        ('Luna', 'Cat', 'Persian', 4, 'None', 'Laid-back', 1),
        ('Rocky', 'Dog', 'Bulldog', 5, 'None', 'Loyal', 2),
        ('Bubbles', 'Fish', 'Betta', 1, 'None', 'Colorful', 3),
        ('Nibbles', 'Hamster', 'Syrian', 2, 'Dust', 'Nocturnal', 4),
    ]
    c.executemany('''
        INSERT OR IGNORE INTO pets (name, species, breed, age, allergen, temperament, owner_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', pets)

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
