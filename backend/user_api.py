from flask import Blueprint, jsonify, request

app = Blueprint('user_api', __name__)

@app.route('/api/register', methods=['POST'])
def register_user():
    return jsonify(request.json)

@app.route('/api/login', methods=['POST'])
def login_user():
    return jsonify({"message": "Logged in"})

@app.route('/api/profile', methods=['GET'])
def get_profile():
    return jsonify({"id": 1, "name": "John Doe", "email": "john@example.com"})

@app.route('/api/profile', methods=['PUT'])
def update_profile():
    return jsonify(request.json)
