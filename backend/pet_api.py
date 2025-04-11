from flask import Blueprint, jsonify, request

app = Blueprint('pet_api', __name__)

pets = [
    {"id": 1, "name": "Buddy", "species": "Dog", "breed": "Labrador"},
    {"id": 2, "name": "Whiskers", "species": "Cat", "breed": "Siamese"}
]

@app.route('/api/pets', methods=['GET'])
def get_pets():
    return jsonify(pets)

@app.route('/api/pets/<int:pet_id>', methods=['GET'])
def get_pet(pet_id):
    pet = next((p for p in pets if p["id"] == pet_id), None)
    return jsonify(pet or {"error": "Pet not found"}), 200 if pet else 404

@app.route('/api/pets/<int:pet_id>/save', methods=['POST'])
def save_pet(pet_id):
    return jsonify({"message": f"Pet {pet_id} saved."})

@app.route('/api/pets/saved', methods=['GET'])
def get_saved_pets():
    return jsonify([])

@app.route('/api/pets/search', methods=['GET'])
def search_pets():
    species = request.args.get('species')
    filtered = [p for p in pets if species.lower() in p["species"].lower()] if species else pets
    return jsonify(filtered)

