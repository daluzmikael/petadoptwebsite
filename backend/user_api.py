from flask import Blueprint, jsonify, request
from db import get_all_users, create_user, get_user_by_email, update_user_profile

'''Users api'''

user_api = Blueprint('user_api', __name__)

@user_api.route('/users', methods=['GET'])
def get_users():
    """
    Get list of all users
    ---
    responses:
      200:
        description: A list of users
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
              name:
                type: string
              email:
                type: string
    """
    
    users = get_all_users()

    return jsonify(users)

@user_api.route('/register', methods=['POST'])
def register_user():
    """
    Register a new user
    ---
    parameters:
      - in: body
        name: user
        schema:
          type: object
          required:
            - name
            - email
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: Confirmation of registration
    """

    data = request.get_json(silent=True) or {}
    name = str(data.get('name', '')).strip()
    email = str(data.get('email', '')).strip().lower()
    password = str(data.get('password', ''))
    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400
    result = create_user(name, email, password)
    if "error" in result:
        return jsonify(result), 409
    return jsonify(result), 201

@user_api.route('/login', methods=['POST'])
def login_user():
    """
    Login user
    ---
    parameters:
      - in: body
        name: credentials
        required: true
        schema:
          type: object
          required:
            - email
          properties:
            email:
              type: string
    responses:
      200:
        description: Login success or failure
    """
    data = request.get_json(silent=True) or {}
    email = str(data.get("email", "")).strip().lower()
    password = str(data.get("password", ""))
    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400
    user = get_user_by_email(email)
    if user and user.get("password") == password:
        public_user = {key: value for key, value in user.items() if key != "password"}
        return jsonify({"message": "Logged in", "user": public_user})
    else:
        return jsonify({"error": "Invalid email or password"}), 404
    


@user_api.route('/profile', methods=['GET'])
def get_profile():
    """
    Get user profile
    ---
    responses:
      200:
        description: User profile data
        schema:
          type: object
          properties:
            id:
              type: integer
            name:
              type: string
            email:
              type: string
    """
    user = get_user_by_email("alice@example.com")  # TEMP: Simulating a logged-in user
    if user:
        return jsonify({key: value for key, value in user.items() if key != "password"})
    else:
        return jsonify({"error": "Profile not found"}), 404
    
@user_api.route('/users/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    """
    Update user profile
    ---
    parameters:
      - in: body
        name: profile
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
    responses:
      200:
        description: Updated profile object
    """
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    email = str(data.get("email", "")).strip().lower()
    if not name or not email:
        return jsonify({"error": "Name and email are required"}), 400
    if not update_user_profile(user_id, name, email):
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user_id, "username": name, "email": email})
