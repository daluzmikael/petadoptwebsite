import { useEffect, useState } from 'react';
import './Adopt.css';

export default function Adopt() {
  const [pets, setPets] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/pets")
      .then((res) => res.json())
      .then((data) => setPets(data))
      .catch((err) => console.error("Failed to fetch pets:", err));
  }, []);

  const handleSave = (id) => {
    fetch(`http://localhost:5000/api/pets/${id}/save`, {
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        alert(data.message || "Pet saved!");
      })
      .catch((err) => console.error("Save failed:", err));
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
