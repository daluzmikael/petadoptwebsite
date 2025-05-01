// src/components/PetCard.jsx
import React from 'react';

function PetCard({ pet }) {
  return (
    <div className="pet-card">
      <h3>{pet.name}</h3>
      <p>Breed: {pet.breed}</p>
      <img src={pet.image} alt={pet.name} />
      <button>Adopt</button>
    </div>
  );
}

export default PetCard;
