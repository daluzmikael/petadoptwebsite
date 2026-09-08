// src/pages/Adopt.jsx

import { useEffect, useState } from 'react';
import './Adopt.css';
import { apiRequest, getPetImage } from '../api';

export default function Adopt() {
  const [pets, setPets] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    apiRequest("/api/pets")
      .then(setPets)
      .catch((err) => setError(err.message));
  }, []);

  const handleSave = (petId) => {
    const userId = localStorage.getItem("userId");

    apiRequest(`/api/pets/${petId}/save`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ user_id: userId })
    })
      .then(data => alert(data.message))
      .catch(err => setError(err.message));
  };

  return (
    <div className="adopt-page">
      <h2 className="adopt-title">Available Pets</h2>
      {error ? <p className="page-error">{error}</p> : null}
      <div className="pets-grid">
        {pets.map((pet) => (
          <div key={pet.id} className="pet-card">
            <img
              src={getPetImage(pet)}
              alt={pet.name}
              className="pet-image"
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
        ))}
      </div>
    </div>
  );
}
