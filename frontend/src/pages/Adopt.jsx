// src/pages/Adopt.jsx

import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Adopt.css';

export default function Adopt() {
  const [pets, setPets] = useState([]);
  const navigate = useNavigate();

  // 🔒 Redirect if not logged in
  useEffect(() => {
    const userId = localStorage.getItem("userId");
    if (!userId) {
      navigate("/?error=login_required");
    }
  }, [navigate]);

  // 🐾 Fetch pets
  useEffect(() => {
    fetch("http://localhost:5000/api/pets")
      .then((res) => res.json())
      .then((data) => setPets(data))
      .catch((err) => console.error("Failed to fetch pets:", err));
  }, []);

  // 💾 Save a pet for this user
  const handleSave = (petId) => {
    const userId = localStorage.getItem("userId");

    fetch(`http://localhost:5000/api/pets/${petId}/save`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ user_id: userId })
    })
      .then(res => res.json())
      .then(data => alert(data.message))
      .catch(err => console.error("Save failed:", err));
  };

  return (
    <div className="adopt-page">
      <h2 className="adopt-title">Available Pets</h2>
      <div className="pets-grid">
        {pets.map((pet) => (
          <div key={pet.id} className="pet-card">
            <img
              src={`/images/${pet.image}`}
              alt={pet.name}
              className="pet-image"
            />
            <h3 className="pet-name">{pet.name}</h3>
            <p className="pet-details">{pet.species} • {pet.breed}</p>
            <button
              className="save-button"
              onClick={() => handleSave(pet.id)}
            >
              Save
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
