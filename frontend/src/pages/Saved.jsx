// src/pages/Saved.jsx

import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Saved() {
  const [savedPets, setSavedPets] = useState([]);
  const userId = localStorage.getItem("userId");
  const navigate = useNavigate();

  // Redirect if not logged in
  useEffect(() => {
    if (!userId) {
      navigate("/?error=login_required");
    }
  }, [userId, navigate]);

  // Fetch saved pets for this user
  useEffect(() => {
    if (userId) {
      fetch(`http://localhost:5000/api/pets/saved/${userId}`)
        .then(res => res.json())
        .then(data => setSavedPets(data))
        .catch(err => console.error("Failed to fetch saved pets:", err));
    }
  }, [userId]);

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6 text-center">Your Saved Pets</h2>
      {savedPets.length === 0 ? (
        <p className="text-center text-gray-600">You haven't saved any pets yet.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          {savedPets.map((pet) => (
            <div key={pet.id} className="border p-4 rounded shadow text-center">
              <h3 className="text-xl font-bold">{pet.name}</h3>
              <p>{pet.species} • {pet.breed}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
