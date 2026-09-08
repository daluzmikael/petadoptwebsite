from flask import Blueprint, jsonify, request
from db import (
    search_pets_by_query,
    get_all_pets,
    get_pet_by_id,
    save_pet_for_user,
    unsave_pet_for_user,
    get_saved_pets_for_user,
)

'''Pets API'''

pet_api = Blueprint('pet_api', __name__)

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
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID required"}), 400
    if not get_pet_by_id(pet_id):
        return jsonify({"error": "Pet not found"}), 404
    try:
        save_pet_for_user(user_id, pet_id)
        return jsonify({"message": f"Pet {pet_id} saved for user {user_id}"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@pet_api.route('/pets/<int:pet_id>/unsave', methods=['DELETE'])
def unsave_pet(pet_id):
    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    if not user_id:
        return jsonify({"error": "User ID required"}), 400
    unsave_pet_for_user(user_id, pet_id)

    return jsonify({"message": f"Pet {pet_id} unsaved for user {user_id}"}), 200

@pet_api.route('/pets/saved/<int:user_id>', methods=['GET'])
def get_saved_pets(user_id):
    pets = get_saved_pets_for_user(user_id)
    return jsonify(pets)

@pet_api.route('/pets/search', methods=['GET'])
def search_pets_by_query_route():
    query = (request.args.get('query') or request.args.get('species') or '').strip()
    if not query:
        return jsonify(get_all_pets())
    results = search_pets_by_query(query)
    return jsonify(results)
