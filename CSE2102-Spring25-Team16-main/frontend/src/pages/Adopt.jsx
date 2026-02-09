// src/pages/Adopt.jsx

import { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './Adopt.css';

export default function Adopt() {
  const navigate = useNavigate();

  const pets = [
    {
      id: 1,
      name: "Max",
      species: "Dog",
      breed: "Labrador"
    },
    {
      id: 2,
      name: "Lily",
      species: "Cat",
      breed: "Siamese"
    },
    {
      id: 3,
      name: "Mr Fluffy",
      species: "Rabbit",
      breed: "Angora"
    }
  ];

  useEffect(() => {
    const userId = localStorage.getItem("userId");
    if (!userId) {
      navigate("/?error=login_required");
    }
  }, [navigate]);

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

  const handleImageError = (e) => {
    e.target.src = '/default.jpg'; 
  };

  return (
    <div className="adopt-page">
      <h2 className="adopt-title">Available Pets</h2>
      <div className="pets-grid">
        {pets.map((pet) => {
          const imageName = `${pet.name.toLowerCase().replace(/\s+/g, '-')}.jpg`;
          return (
            <div key={pet.id} className="pet-card">
              <img
                src={`/${imageName}`}
                alt={pet.name}
                className="pet-image"
                onError={handleImageError}
              />
              <h3 className="pet-name">{pet.name}</h3>
              <p className="pet-details">{pet.species} - {pet.breed}</p>
              <button
                className="save-button"
                onClick={() => handleSave(pet.id)}
              >
                Save
              </button>
            </div>
          );
        })}
      </div>
    </div>
  );
}
