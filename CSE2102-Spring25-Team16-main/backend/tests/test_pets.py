# 1. Get all pets
def test_get_pets():
    response = requests.get(f"{BASE_URL}/api/pets")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# 2. Get pet by ID (existing)
def test_get_pet_success():
    response = requests.get(f"{BASE_URL}/api/pets/1")
    assert response.status_code == 200
    assert "name" in response.json()

# 3. Get pet by ID (nonexistent)
def test_get_pet_not_found():
    response = requests.get(f"{BASE_URL}/api/pets/9999")
    assert response.status_code == 404
    assert "error" in response.json()

# 4. Search pets by species
def test_search_pets():
    response = requests.get(f"{BASE_URL}/api/pets/search?species=cat")
    assert response.status_code == 200
    for pet in response.json():
        assert "cat" in pet["species"].lower()

# 5. Save pet
def test_save_pet():
    response = requests.post(f"{BASE_URL}/api/pets/1/save")
    assert response.status_code == 200
    assert "saved" in response.json()["message"].lower()

# 6. Get saved pets
def test_get_saved_pets():
    response = requests.get(f"{BASE_URL}/api/pets/saved")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

