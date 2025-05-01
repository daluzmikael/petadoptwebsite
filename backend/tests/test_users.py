import uuid
import requests

BASE_URL = "http://localhost:5000"

# 1. Register a user (success)
def test_register_user():
    email = f"test_{uuid.uuid4().hex}@example.com"
    response = requests.post(f"{BASE_URL}/api/register", json={"name": "Test User", "email": email})
    assert response.status_code == 200
    assert response.json()["email"] == email

# 2. Register user (missing email)
def test_register_missing_email():
    response = requests.post(f"{BASE_URL}/api/register", json={"name": "No Email"})
    assert response.status_code != 200

# 3. Login success
def test_login_user():
    email = f"test_{uuid.uuid4().hex}@example.com"
    requests.post(f"{BASE_URL}/api/register", json={"name": "Login Test", "email": email})
    response = requests.post(f"{BASE_URL}/api/login", json={"email": email})
    assert response.status_code == 200
    assert response.json()["message"] == "Logged in"

# 4. Login fail (email not found)
def test_login_fail_invalid_email():
    response = requests.post(f"{BASE_URL}/api/login", json={"email": "nonexistent@example.com"})
    assert response.status_code == 404
    assert "error" in response.json()

# 5. Get profile (hardcoded user ID 1)
def test_get_profile():
    response = requests.get(f"{BASE_URL}/api/profile")
    assert response.status_code == 200
    assert "username" in response.json()

# 6. Update profile (user ID 1)
def test_update_profile():
    payload = {"name": "Updated User", "email": "updated@example.com"}
    response = requests.put(f"{BASE_URL}/api/profile", json=payload)
    assert response.status_code == 200
    assert response.json()["email"] == "updated@example.com"

# 7. Get all users
def test_get_all_users():
    response = requests.get(f"{BASE_URL}/api/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

