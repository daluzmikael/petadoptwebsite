from flask import Blueprint, jsonify, request
from db import get_all_pets, get_pet_by_id, search_pets_by_species, save_pet_for_user, get_saved_pets_for_user

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
    pets = get_all_pets()
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
    pet = get_pet_by_id(pet_id)
    if pet:
        return jsonify(pet)
    else:
        return jsonify({"error": "Pet not found"}), 404

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
    user_id = 1  # Simulated logged-in user
    save_pet_for_user(user_id, pet_id)
    return jsonify({"message": f"Pet {pet_id} saved for user {user_id}."})

@pet_api.route('/api/pets/saved', methods=['GET'])
def get_saved_pets():
    """
    Get saved pets (currently always empty)
    ---
    responses:
      200:
        description: List of saved pets
    """
    user_id = 1  # Simulated logged-in user
    pets = get_saved_pets_for_user(user_id)
    return jsonify(pets)

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
    pets = search_pets_by_species(species) if species else get_all_pets()
    return jsonify(pets)
