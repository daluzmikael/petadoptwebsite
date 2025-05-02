import { useEffect, useState } from 'react';
import PetCard from '../components/petcard';
import './Saved.css';

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
    <div className="saved-page">
      <h2 className="saved-title">Your Saved Pets</h2>
      {savedPets.length === 0 ? (
        <p className="saved-empty">You have no saved pets yet.</p>
      ) : (
        <div className="saved-grid">
          {savedPets.map((pet, index) => (
            <PetCard
              key={index}
              name={pet.name}
              species={pet.species}
              breed={pet.breed || "Unknown"}
              image={pet.image}
            />
          ))}
        </div>
      )}
    </div>
  );
}
