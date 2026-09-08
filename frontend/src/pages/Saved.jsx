import { useEffect, useState } from "react";
import "./Saved.css";
import { apiRequest, getPetImage } from "../api";

export default function Saved() {
  const [pets, setPets] = useState([]);
  const [events, setEvents] = useState([]);
  const [error, setError] = useState('');
  const userId = localStorage.getItem("userId");

  useEffect(() => {
    Promise.all([
      apiRequest(`/api/pets/saved/${userId}`),
      apiRequest(`/api/events/rsvped/${userId}`),
    ])
      .then(([savedPets, savedEvents]) => {
        setPets(savedPets);
        setEvents(savedEvents);
      })
      .catch(err => setError(err.message));
  }, [userId]);

  const handleUnsavePet = (petId) => {
    apiRequest(`/api/pets/${petId}/unsave`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId }),
    })
      .then(data => {
        alert(data.message);
        setPets(prev => prev.filter(pet => pet.id !== petId));
      })
      .catch(err => setError(err.message));
  };

  const handleUnRSVP = (eventId) => {
    apiRequest(`/api/events/${eventId}/rsvp`, {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId }),
    })
      .then(data => {
        alert(data.message);
        setEvents(prev => prev.filter(e => e.id !== eventId));
      })
      .catch(err => setError(err.message));
  };

  return (
    <div className="saved-page">
      <h2 className="saved-title">Your Saved Pets & Events</h2>
      {error ? <p className="page-error">{error}</p> : null}

      <h3 className="saved-section-title">Saved Pets</h3>
      {pets.length === 0 ? <p className="saved-empty">No saved pets yet.</p> : null}
      <div className="saved-grid">
        {pets.map(p => (
          <div key={p.id} className="pet-card">
            <img
              src={getPetImage(p)}
              className="pet-image"
              alt={p.name || "Saved Pet"}
            />
            <p className="pet-name">{p.name}</p>
            <p>{p.species}</p>
            <button
              className="save-button"
              onClick={() => handleUnsavePet(p.id)}
            >
              Unsave Pet
            </button>
          </div>
        ))}
      </div>

      <h3 className="saved-section-title">Event RSVPs</h3>
      {events.length === 0 ? <p className="saved-empty">No event RSVPs yet.</p> : null}
      <div className="saved-grid">
        {events.map(e => (
          <div key={e.id} className="pet-card">
            <p className="pet-name">{e.name}</p>
            <p>{e.date}</p>
            <button
              className="save-button"
              onClick={() => handleUnRSVP(e.id)}
            >
              Remove RSVP
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
