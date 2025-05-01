from flask import Blueprint, jsonify, request
'''Users api'''

user_api = Blueprint('user_api', __name__)

@user_api.route('/api/users', methods=['GET'])
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
    
    users = [
        {"id": 1, "name": "John Doe", "email": "john@example.com"},
        {"id": 2, "name": "Jane Smith", "email": "jane@example.com"}
    ]
    return jsonify(users)

@user_api.route('/api/register', methods=['POST'])
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
    return jsonify(request.json)

@user_api.route('/api/login', methods=['POST'])
def login_user():
    """
    Login user
    ---
    responses:
      200:
        description: Login success message
    """
    return jsonify({"message": "Logged in"})

@user_api.route('/api/profile', methods=['GET'])
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
    return jsonify({"id": 1, "name": "John Doe", "email": "john@example.com"})

@user_api.route('/api/profile', methods=['PUT'])
def update_profile():
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
    return jsonify(request.json)

