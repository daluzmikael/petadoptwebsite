from flask import Blueprint, jsonify, request
from db import (
    get_connection,
    get_all_pets,
    get_pet_by_id,
    search_pets_by_species,
    search_pets_by_query,
    save_pet_for_user,
    get_saved_pets_for_user
)

'''Pets API Blueprint'''
pet_api = Blueprint('pet_api', __name__)

# Get all pets
@pet_api.route('/api/pets', methods=['GET'])
def get_pets():
    pets = get_all_pets()
    return jsonify(pets)

# Get pet by ID
@pet_api.route('/api/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet)
    return jsonify({"error": "Pet not found"}), 404

# Save a pet for a user
@pet_api.route('/api/pets/<int:pet_id>/save', methods=['POST'])
def save_pet(pet_id):
    data = request.get_json()
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO saved_pets (user_id, pet_id) VALUES (?, ?)", (user_id, pet_id))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Pet {pet_id} saved for user {user_id}"}), 200


@pet_api.route('/pets/saved/<int:user_id>', methods=['GET'])
def get_saved_pets(user_id):
    conn = get_connection()
    c = conn.cursor()
    c.execute('''
        SELECT pets.id, pets.name, pets.species
        FROM pets
        JOIN saved_pets ON pets.id = saved_pets.pet_id
        WHERE saved_pets.user_id = ?
    ''', (user_id,))
    pets = c.fetchall()
    conn.close()

    return jsonify([
        {"id": p[0], "name": p[1], "species": p[2]} for p in pets
    ])


def search_pets_by_query(query):
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        SELECT id, name, species, breed, age, allergen, temperament
        FROM pets
        WHERE 
            species LIKE ? OR 
            breed LIKE ? OR 
            CAST(age AS TEXT) LIKE ? OR 
            allergen LIKE ? OR 
            temperament LIKE ?
    """, (f"%{query}%",)*5)
    rows = c.fetchall()
    conn.close()
    return [
        {
            "id": row[0], "name": row[1], "species": row[2],
            "breed": row[3], "age": row[4],
            "allergen": row[5], "temperament": row[6]
        }
        for row in rows
    ]


# Unsave a pet for a user
@pet_api.route('/api/pets/<int:pet_id>/unsave', methods=['DELETE'])
def unsave_pet(pet_id):
    data = request.get_json()
    user_id = data.get("user_id")

    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400

    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM saved_pets WHERE user_id = ? AND pet_id = ?", (user_id, pet_id))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Pet {pet_id} unsaved for user {user_id}"}), 200

# Get all saved pets for a user
@pet_api.route('/api/pets/saved/<int:user_id>', methods=['GET'])
def get_saved_pets(user_id):
    pets = get_saved_pets_for_user(user_id)
    return jsonify(pets)

# Search pets by species or general query
@pet_api.route('/api/pets/search', methods=['GET'])
def search_pets():
    query = request.args.get('query')
    species = request.args.get('species')

    if query:
        pets = search_pets_by_query(query)
    elif species:
        pets = search_pets_by_species(species)
    else:
        pets = get_all_pets()

    return jsonify(pets)
