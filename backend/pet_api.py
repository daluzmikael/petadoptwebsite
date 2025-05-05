from flask import Blueprint, jsonify, request
from db import search_pets_by_query, get_connection, get_all_pets, get_pet_by_id, search_pets_by_species, save_pet_for_user, get_saved_pets_for_user

'''Pets api'''

pet_api = Blueprint('pet_api', __name__)

pets = [
    {"id": 1, "name": "Buddy", "species": "Dog"},
    {"id": 2, "name": "Whiskers", "species": "Cat"}
]

@pet_api.route('/pets', methods=['GET'])
def get_pets():
    """
    Get list of all pets
    ---
    responses:
      200:
        description: A list of pets
    """
    pets = get_all_pets()
    return jsonify(pets)

@pet_api.route('/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    """
    Get a pet by ID
    ---
    parameters:
      - name: pet_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Pet details or error
    """
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"error": "Pet not found"}), 404

@pet_api.route('/pets/<int:pet_id>/save', methods=['POST'])
def save_pet(pet_id):
    """
    Save a pet by ID
    ---
    parameters:
      - name: pet_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Confirmation message
    """
    data = request.get_json()
    user_id = data.get("user_id")

    try:
        conn = get_connection()
        c = conn.cursor()
        c.execute("INSERT INTO saved_pets (user_id, pet_id) VALUES (?, ?)", (user_id, pet_id))
        conn.commit()
    except sqlite3.OperationalError as e:
        if "database is locked" in str(e):
            return jsonify({"error": "Database is busy. Please try again shortly."}), 503
        else:
            return jsonify({"error": str(e)}), 500
    finally:
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



@pet_api.route('/pets/search', methods=['GET'])
def search_pets_by_query_route():
    query = request.args.get('query', '').strip()
    if not query:
        return jsonify(get_all_pets())
    results = search_pets_by_query(query)
    print(f"Query: {query}, Matches: {len(results)}")
    return jsonify(results)



@pet_api.route('/pets/<int:pet_id>/unsave', methods=['DELETE'])
def unsave_pet(pet_id):
    data = request.get_json()
    user_id = data.get("user_id")

    conn = get_connection()
    c = conn.cursor()
    c.execute("DELETE FROM saved_pets WHERE user_id = ? AND pet_id = ?", (user_id, pet_id))
    conn.commit()
    conn.close()

    return jsonify({"message": f"Pet {pet_id} unsaved for user {user_id}"}), 200

