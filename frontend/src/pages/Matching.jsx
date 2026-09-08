import { useEffect, useState } from "react";
import { apiRequest, getPetImage } from "../api";
import "./Matching.css";

export default function Matching() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [error, setError] = useState("");

  // Fetch all pets on load
  useEffect(() => {
    apiRequest("/api/pets")
      .then(setResults)
      .catch(err => setError(err.message));
  }, []);

  const handleSearch = () => {
    setError("");
    const path = query.trim()
      ? `/api/pets/search?query=${encodeURIComponent(query.trim())}`
      : "/api/pets";
    apiRequest(path)
      .then(setResults)
      .catch(err => setError(err.message));
  };

  return (
    <div className="matching-page">
      <h2 className="matching-title">Pet Compatibility Matching</h2>

      <form className="matching-search" onSubmit={(event) => { event.preventDefault(); handleSearch(); }}>
        <input
          type="text"
          placeholder="Search for cats, golden retrievers, calm, age 3..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="matching-input"
        />
        <button
          type="submit"
          className="matching-button"
        >
          Search
        </button>
      </form>

      {error ? <p className="page-error">{error}</p> : null}

      {results.length === 0 ? (
        <p className="matching-empty">No pets found.</p>
      ) : (
        <div className="matching-grid">
          {results.map(pet => (
            <div key={pet.id} className="matching-card">
              <img src={getPetImage(pet)} alt={pet.name} className="matching-image" />
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
