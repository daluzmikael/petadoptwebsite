import sqlite3

DB_NAME = 'database.db'

def get_connection():
    return sqlite3.connect(DB_NAME)

def get_all_users():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "username": row[1], "email": row[2]} for row in rows]

def get_user_by_email(email):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = c.fetchone()
    conn.close()
    return {"id": row[0], "username": row[1], "email": row[2]} if row else None

def create_user(name, email):
    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO users (username, email) VALUES (?, ?)", (name, email))
        conn.commit()
        user_id = c.lastrowid
        conn.close()
        return {"id": user_id, "username": name, "email": email}
    except sqlite3.IntegrityError as e:
        return {"error": str(e)}

def update_user_profile(user_id, name, email):
    conn = get_connection()
    c = conn.cursor()
    c.execute("UPDATE users SET username = ?, email = ? WHERE id = ?", (name, email, user_id))
    conn.commit()
    conn.close()

def get_all_pets():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, species FROM pets")
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "species": row[2]} for row in rows]

def get_pet_by_id(pet_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, species FROM pets WHERE id = ?", (pet_id,))
    row = c.fetchone()
    conn.close()
    return {"id": row[0], "name": row[1], "species": row[2]} if row else None

def search_pets_by_species(species):
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT id, name, species FROM pets WHERE species LIKE ?", (f"%{species}%",))
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "species": row[2]} for row in rows]

def save_pet_for_user(user_id, pet_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO saved_pets (user_id, pet_id) VALUES (?, ?)", (user_id, pet_id))
    conn.commit()
    conn.close()

def get_saved_pets_for_user(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT pets.id, pets.name, pets.species
        FROM pets
        JOIN saved_pets ON pets.id = saved_pets.pet_id
        WHERE saved_pets.user_id = ?
    """, (user_id,))
    rows = c.fetchall()
    conn.close()
    return [{"id": row[0], "name": row[1], "species": row[2]} for row in rows]

