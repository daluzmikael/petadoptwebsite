// src/pages/Adopt.jsx

import { useEffect, useState } from 'react';

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
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6 text-center">Available Pets</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {pets.map((pet) => (
          <div
            key={pet.id}
            className="border p-4 rounded shadow text-center bg-white"
          >
            <h3 className="text-xl font-bold">{pet.name}</h3>
            <p>{pet.species} • {pet.breed}</p>
            <button
              className="mt-3 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
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
