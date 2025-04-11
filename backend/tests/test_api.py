import requests
# Backend tests go here

BASE_URL = "http://localhost:5000"

def test_register_user():
    payload = {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "secure123"
    }
    response = requests.post(f"{BASE_URL}/api/register", json=payload)
    assert response.status_code == 200
    assert response.json()["email"] == "john@example.com"

def test_login_user():
    response = requests.post(f"{BASE_URL}/api/login", json={"email": "john@example.com", "password": "secure123"})
    assert response.status_code == 200
    assert response.json()["message"] == "Logged in"

def test_get_profile():
    response = requests.get(f"{BASE_URL}/api/profile")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John Doe"
    assert data["email"] == "john@example.com"

def test_update_profile():
    new_data = {"name": "John Updated", "email": "john_updated@example.com"}
    response = requests.put(f"{BASE_URL}/api/profile", json=new_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"

# Pets ----

def test_get_pets():
    response = requests.get(f"{BASE_URL}/api/pets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_pet_success():
    response = requests.get(f"{BASE_URL}/api/pets/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Buddy"

def test_get_pet_not_found():
    response = requests.get(f"{BASE_URL}/api/pets/999")
    assert response.status_code == 404
    assert response.json()["error"] == "Pet not found"

def test_save_pet():
    response = requests.post(f"{BASE_URL}/api/pets/1/save")
    assert response.status_code == 200
    assert "saved" in response.json()["message"]

def test_search_pets():
    response = requests.get(f"{BASE_URL}/api/pets/search?species=dog")
    assert response.status_code == 200
    pets = response.json()
    assert all("Dog" in p["species"] for p in pets)
