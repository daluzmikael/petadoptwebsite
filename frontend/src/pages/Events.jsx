// src/pages/Events.jsx
import { useState, useEffect } from 'react';
import EventCard from '../components/EventCard';

export default function Events() {
  const [events, setEvents] = useState([]);
  const userId = localStorage.getItem("userId");

  useEffect(() => {
    fetch("http://localhost:5000/api/events")
      .then(res => res.json())
      .then(data => setEvents(data))
      .catch(err => console.error("Failed to fetch events:", err));
  }, []);

  const handleRSVP = (eventId) => {
    fetch(`http://localhost:5000/api/events/${eventId}/rsvp`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId })
    })
      .then(res => res.json())
      .then(data => alert(data.message))
      .catch(err => console.error("RSVP error:", err));
  };

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6 text-center">Upcoming Events</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
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
