// src/pages/Matching.jsx
import { useState } from "react";
import './Matching.css';

export default function Matching() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = () => {
    if (!query.trim()) return;

    fetch(`http://localhost:5000/api/pets/search?query=${encodeURIComponent(query)}`)
      .then(res => res.json())
      .then(data => setResults(data))
      .catch(err => console.error("Search failed:", err));
  };

  return (
    <div className="matching-page">
      <h2 className="matching-title">Pet Compatibility Matching</h2>

      <div className="matching-search">
        <input
          type="text"
          placeholder="Search for cats, golden retrievers, calm, age 3..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="matching-input"
        />
        <button onClick={handleSearch} className="matching-button">
          Search
        </button>
      </div>

      {results.length === 0 ? (
        <p className="matching-empty">No pets found. Try searching by species, breed, temperament, or age.</p>
      ) : (
        <div className="matching-grid">
          {results.map((pet) => (
            <div key={pet.id} className="matching-card">
              <img src={`/images/${pet.image || "placeholder.jpg"}`} alt={pet.name} className="matching-image" />
              <p className="matching-name">{pet.name}</p>
              <p className="matching-info">{pet.species} • {pet.breed} • Age {pet.age}</p>
              <p className="matching-temperament">{pet.temperament}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
