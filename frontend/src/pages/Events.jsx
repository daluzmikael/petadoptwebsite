import { useState, useEffect } from 'react';
import './Events.css';
import { apiRequest } from '../api';

function EventCard({ title, date, location, onRSVP }) {
  return (
    <div className="event-card">
      <h3 className="event-title">{title}</h3>
      <p className="event-details">📅 {date}</p>
      <p className="event-details">📍 {location}</p>
      <button className="event-button" onClick={onRSVP}>RSVP</button>
    </div>
  );
}

export default function Events() {
  const [events, setEvents] = useState([]);
  const [error, setError] = useState('');
  const userId = localStorage.getItem("userId");

  useEffect(() => {
    apiRequest("/api/events")
      .then(setEvents)
      .catch(err => setError(err.message));
  }, []);

  const handleRSVP = (eventId) => {
    apiRequest(`/api/events/${eventId}/rsvp`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId })
    })
      .then(data => alert(data.message))
      .catch(err => setError(err.message));
  };

  return (
    <div className="events-page">
      <h2 className="events-title">Upcoming Events</h2>
      {error ? <p className="page-error">{error}</p> : null}
      <div className="events-grid">
        {events.map((event) => (
          <EventCard
            key={event.id}
            title={event.name}
            date={event.date}
            location={event.location || "Location TBD"}
            onRSVP={() => handleRSVP(event.id)}
          />
        ))}
      </div>
    </div>
  );
}
