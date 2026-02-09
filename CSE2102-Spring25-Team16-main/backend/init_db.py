import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Users table 
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    ''')

    # Pets table
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
            image TEXT NOT NULL,
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

    # Extra info
    c.execute('''
        CREATE TABLE IF NOT EXISTS extra (
            id INTEGER PRIMARY KEY,
            info TEXT NOT NULL
        )
    ''')

    # Sample users 
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

    # Sample pets
    pets = [
        ('Max', 'Dog', 'Golden Retriever', 3, 'None', 'family-friendly', 1, '/public/max.jpg'),
        ('Lily', 'Cat', 'Siamese', 2, 'None', 'quiet', 2, '/public/lily.jpg'),
        ('Bella', 'Dog', 'Beagle', 5, 'None', 'energetic', 3, '/public/bella.jpg'),
        ('Shadow', 'Cat', 'Persian', 4, 'None', 'calm', 4, '/public/shadow.jpg'),
        ('Oreo', 'Rabbit', 'Dutch', 1, 'Hay', 'quiet', 5, '/public/oreo.jpg'),
        ('Coco', 'Dog', 'French Bulldog', 3, 'None', 'loyal', 6, '/placeholder.jpg'),
        ('Pepper', 'Cat', 'Bengal', 2, 'None', 'playful', 7, '/placeholder.jpg'),
        ('Milo', 'Hamster', 'Syrian', 1, 'Dust', 'independent', 8, '/placeholder.jpg'),
        ('Rex', 'Dog', 'Rottweiler', 6, 'None', 'not-kid-friendly', 1, '/placeholder.jpg'),
        ('Whiskers', 'Cat', 'Tabby', 5, 'None', 'family-friendly', 2, '/placeholder.jpg'),
        ('Blue', 'Parrot', 'Macaw', 4, 'Feathers', 'loud', 3, '/placeholder.jpg'),
        ('Finn', 'Fish', 'Betta', 1, 'None', 'calm', 4, '/placeholder.jpg'),
        ('Hazel', 'Dog', 'Husky', 4, 'None', 'energetic', 5, '/placeholder.jpg'),
        ('Nugget', 'Rabbit', 'Lop', 2, 'Hay', 'quiet', 6, '/placeholder.jpg'),
        ('Ginger', 'Cat', 'Maine Coon', 3, 'None', 'loyal', 7, '/placeholder.jpg'),
        ('Tank', 'Dog', 'Bulldog', 5, 'None', 'calm', 8, '/placeholder.jpg'),
        ('Daisy', 'Dog', 'Poodle', 4, 'None', 'playful', 1, '/placeholder.jpg'),
        ('Snowball', 'Cat', 'Ragdoll', 3, 'None', 'family-friendly', 2, '/placeholder.jpg'),
        ('Winston', 'Dog', 'Corgi', 2, 'None', 'energetic', 3, '/placeholder.jpg'),
        ('Basil', 'Cat', 'British Shorthair', 6, 'None', 'quiet', 4, '/placeholder.jpg'),
        ('Mocha', 'Dog', 'Chihuahua', 3, 'None', 'loud', 5, '/placeholder.jpg'),
        ('Poppy', 'Rabbit', 'Mini Rex', 2, 'Hay', 'independent', 6, '/placeholder.jpg'),
        ('Zazu', 'Parrot', 'Cockatoo', 4, 'Feathers', 'loud', 7, '/placeholder.jpg'),
        ('Buster', 'Dog', 'Boxer', 5, 'None', 'not-kid-friendly', 8, '/placeholder.jpg')
    ]

    c.executemany(
        "INSERT OR IGNORE INTO pets (name, species, breed, age, allergen, temperament, owner_id, image) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        pets
    )

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
