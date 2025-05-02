from flask import Blueprint, jsonify, request
from db import get_connection, get_all_pets, get_pet_by_id, search_pets_by_species

'''Pets API'''
pet_api = Blueprint('pet_api', __name__)


pets = [
    {"id": 1, "name": "Buddy", "species": "Dog"},
    {"id": 2, "name": "Whiskers", "species": "Cat"}
]

@pet_api.route('/api/pets', methods=['GET'])

@pet_api.route('/pets', methods=['GET'])

def get_pets():
    pets = get_all_pets()
    return jsonify(pets)

@pet_api.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"error": "Pet not found"}), 404

@pet_api.route('/pets/<int:pet_id>/save', methods=['POST'])
def save_pet(pet_id):
    data = request.get_json()
    user_id = data.get("user_id")

    print("SAVING PET:", pet_id, "FOR USER:", user_id)

    conn = get_connection()
    c = conn.cursor()

    c.execute("SELECT 1 FROM saved_pets WHERE user_id = ? AND pet_id = ?", (user_id, pet_id))
    if not c.fetchone():
        c.execute("INSERT INTO saved_pets (user_id, pet_id) VALUES (?, ?)", (user_id, pet_id))
        conn.commit()

    conn.close()
    return jsonify({"message": f"Pet {pet_id} saved for user {user_id}"})


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

@pet_api.route('/pets/search', methods=['GET'])
def search_pets():
    species = request.args.get('species')
    pets = search_pets_by_species(species) if species else get_all_pets()
    return jsonify(pets)
