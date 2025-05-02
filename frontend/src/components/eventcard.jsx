// src/components/eventcard.jsx
import React from 'react';

export default function EventCard({ title, date, location, index }) {
  const userId = localStorage.getItem("userId");

  const handleRSVP = () => {
    fetch(`http://localhost:5000/api/events/${index + 1}/rsvp`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId }),
    })
      .then((res) => res.json())
      .then((data) => alert(data.message))
      .catch((err) => console.error("RSVP failed:", err));
  };

  return (
    <div className="border p-4 rounded shadow bg-white text-center">
      <h3 className="text-xl font-bold">{title}</h3>
      <p className="text-sm text-gray-600">{date}</p>
      <p className="text-sm text-gray-600">{location}</p>
      <button
        onClick={handleRSVP}
        className="mt-4 px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
      >
        RSVP
      </button>
    </div>
  );
}
