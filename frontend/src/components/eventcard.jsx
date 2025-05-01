// src/components/EventCard.jsx
import React from 'react';

function EventCard({ event }) {
  return (
    <div className="event-card">
      <h3>{event.title}</h3>
      <p>{event.date}</p>
      <p>{event.description}</p>
      <button>Learn More</button>
    </div>
  );
}

export default EventCard;
