// src/pages/Matching.jsx
import { useState } from "react";

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
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Pet Compatibility Matching</h2>

      <div className="flex items-center gap-2 mb-6">
        <input
          type="text"
          placeholder="Search for cats, golden retrievers, calm, age 3..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          className="flex-1 border p-2 rounded"
        />
        <button
          onClick={handleSearch}
          className="bg-blue-600 text-white px-4 py-2 rounded"
        >
          Search
        </button>
      </div>

      {results.length === 0 ? (
        <p className="text-gray-600 text-center">No pets found. Try searching by species, breed, temperament, or age.</p>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          {results.map(pet => (
            <div key={pet.id} className="border p-2 rounded shadow">
              <img src="/placeholder.jpg" alt={pet.name} className="w-full h-32 object-cover rounded" />
              <p className="text-center mt-2 font-bold">{pet.name}</p>
              <p className="text-center text-sm">{pet.species} • {pet.breed} • Age {pet.age}</p>
              <p className="text-center text-xs text-gray-500">{pet.temperament}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
