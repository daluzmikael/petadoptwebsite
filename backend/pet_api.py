from flask import Blueprint, jsonify, request
'''Pets api'''

pet_api = Blueprint('pet_api', __name__)

pets = [
    {"id": 1, "name": "Buddy", "species": "Dog", "breed": "Labrador"},
    {"id": 2, "name": "Whiskers", "species": "Cat", "breed": "Siamese"}
]

@pet_api.route('/api/pets', methods=['GET'])
def get_pets():
    """
    Get list of all pets
    ---
    responses:
      200:
        description: A list of pets
    """
    return jsonify(pets)

@pet_api.route('/api/pets/<int:pet_id>', methods=['GET'])
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
    pet = next((p for p in pets if p["id"] == pet_id), None)
    return jsonify(pet or {"error": "Pet not found"}), 200 if pet else 404

@pet_api.route('/api/pets/<int:pet_id>/save', methods=['POST'])
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
    return jsonify({"message": f"Pet {pet_id} saved."})

@pet_api.route('/api/pets/saved', methods=['GET'])
def get_saved_pets():
    """
    Get saved pets (currently always empty)
    ---
    responses:
      200:
        description: List of saved pets
    """
    return jsonify([])

@pet_api.route('/api/pets/search', methods=['GET'])
def search_pets():
    """
    Search pets by species
    ---
    parameters:
      - name: species
        in: query
        type: string
        required: false
    responses:
      200:
        description: Filtered list of pets
    """    
    species = request.args.get('species')
    filtered = [p for p in pets if species.lower() in p["species"].lower()] if species else pets
    return jsonify(filtered)

