// src/pages/Saved.jsx

import { useEffect, useState } from 'react';
import PetCard from '../components/petcard';

export default function Saved() {
  const [savedPets, setSavedPets] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/api/pets/saved")
      .then(res => res.json())
      .then(data => setSavedPets(data))
      .catch(err => {
        console.error("Failed to fetch saved pets:", err);
      });
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6 text-center">Your Saved Pets</h2>
      {savedPets.length === 0 ? (
        <p className="text-center text-gray-600">You have no saved pets yet.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {savedPets.map((pet, index) => (
            <PetCard
              key={index}
              name={pet.name}
              species={pet.species}
              breed={pet.breed || "Unknown"}
            />
          ))}
        </div>
      )}
    </div>
  );
}
