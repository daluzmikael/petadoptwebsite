import os
import sqlite3
from contextlib import contextmanager
from pathlib import Path


DB_PATH = Path(
    os.environ.get("PET_ADOPTION_DB_PATH", Path(__file__).resolve().parent / "database.db")
)


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


@contextmanager
def database_connection():
    conn = get_connection()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def get_all_users():
    with database_connection() as conn:
        rows = conn.execute("SELECT id, username, email FROM users").fetchall()
    return [{"id": row[0], "username": row[1], "email": row[2]} for row in rows]


def get_user_by_email(email):
    with database_connection() as conn:
        row = conn.execute(
            "SELECT id, username, email, password FROM users WHERE email = ?", (email,)
        ).fetchone()
    if not row:
        return None
    return {"id": row[0], "username": row[1], "email": row[2], "password": row[3]}


def create_user(username, email, password):
    try:
        with database_connection() as conn:
            cursor = conn.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password),
            )
            user_id = cursor.lastrowid
        return {
            "id": user_id,
            "message": "User created",
            "username": username,
            "email": email,
        }
    except sqlite3.IntegrityError:
        return {"error": "Email or username already exists"}


def update_user_profile(user_id, username, email):
    with database_connection() as conn:
        cursor = conn.execute(
            "UPDATE users SET username = ?, email = ? WHERE id = ?",
            (username, email, user_id),
        )
        updated = cursor.rowcount > 0
    return updated


PET_COLUMNS = "id, name, species, breed, age, allergen, temperament, image"


def _pet_from_row(row):
    return {
        "id": row[0],
        "name": row[1],
        "species": row[2],
        "breed": row[3],
        "age": row[4],
        "allergen": row[5],
        "temperament": row[6],
        "image": row[7],
    }


def get_all_pets():
    with database_connection() as conn:
        rows = conn.execute(f"SELECT {PET_COLUMNS} FROM pets").fetchall()
    return [_pet_from_row(row) for row in rows]


def get_pet_by_id(pet_id):
    with database_connection() as conn:
        row = conn.execute(
            f"SELECT {PET_COLUMNS} FROM pets WHERE id = ?", (pet_id,)
        ).fetchone()
    return _pet_from_row(row) if row else None


def search_pets_by_species(species):
    with database_connection() as conn:
        rows = conn.execute(
            f"SELECT {PET_COLUMNS} FROM pets WHERE species LIKE ?",
            (f"%{species}%",),
        ).fetchall()
    return [_pet_from_row(row) for row in rows]


def search_pets_by_query(query):
    wildcard = f"%{query.lower()}%"
    with database_connection() as conn:
        rows = conn.execute(
            f"""
            SELECT {PET_COLUMNS}
            FROM pets
            WHERE LOWER(name) LIKE ?
               OR LOWER(species) LIKE ?
               OR LOWER(breed) LIKE ?
               OR LOWER(temperament) LIKE ?
               OR LOWER(allergen) LIKE ?
               OR CAST(age AS TEXT) LIKE ?
            """,
            (wildcard, wildcard, wildcard, wildcard, wildcard, wildcard),
        ).fetchall()
    return [_pet_from_row(row) for row in rows]


def save_pet_for_user(user_id, pet_id):
    with database_connection() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO saved_pets (user_id, pet_id) VALUES (?, ?)",
            (user_id, pet_id),
        )


def unsave_pet_for_user(user_id, pet_id):
    with database_connection() as conn:
        conn.execute(
            "DELETE FROM saved_pets WHERE user_id = ? AND pet_id = ?",
            (user_id, pet_id),
        )


def get_saved_pets_for_user(user_id):
    with database_connection() as conn:
        rows = conn.execute(
            """
            SELECT pets.id, pets.name, pets.species, pets.breed, pets.age,
                   pets.allergen, pets.temperament, pets.image
            FROM pets
            JOIN saved_pets ON pets.id = saved_pets.pet_id
            WHERE saved_pets.user_id = ?
            """,
            (user_id,),
        ).fetchall()
    return [_pet_from_row(row) for row in rows]


def save_rsvp_for_user(user_id, event_id):
    with database_connection() as conn:
        conn.execute(
            "INSERT OR IGNORE INTO rsvped_events (user_id, event_id) VALUES (?, ?)",
            (user_id, event_id),
        )


def remove_rsvp_for_user(user_id, event_id):
    with database_connection() as conn:
        conn.execute(
            "DELETE FROM rsvped_events WHERE user_id = ? AND event_id = ?",
            (user_id, event_id),
        )


def get_rsvped_events_for_user(user_id):
    with database_connection() as conn:
        rows = conn.execute(
            """
            SELECT events.id, events.name, events.date
            FROM events
            JOIN rsvped_events ON events.id = rsvped_events.event_id
            WHERE rsvped_events.user_id = ?
            """,
            (user_id,),
        ).fetchall()
    return [{"id": row[0], "name": row[1], "date": row[2]} for row in rows]


def get_all_events():
    with database_connection() as conn:
        rows = conn.execute("SELECT id, name, date FROM events ORDER BY date").fetchall()
    return [{"id": row[0], "name": row[1], "date": row[2]} for row in rows]


def save_questionnaire_responses(user_id, responses):
    with database_connection() as conn:
        conn.executemany(
            "INSERT INTO questionnaire_responses (user_id, question, answer) VALUES (?, ?, ?)",
            [(user_id, question, answer) for question, answer in responses],
        )


def get_questionnaire_responses():
    with get_connection() as conn:
        rows = conn.execute(
            "SELECT user_id, question, answer FROM questionnaire_responses"
        ).fetchall()
    return [
        {"user_id": row[0], "question": row[1], "answer": row[2]} for row in rows
    ]
