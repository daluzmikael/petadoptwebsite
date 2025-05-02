// src/components/eventcard.jsx

import React from 'react';

export default function EventCard({ title, date, location }) {
  return (
    <div className="border p-4 rounded shadow bg-white text-center">
      <h3 className="text-xl font-bold">{title}</h3>
      <p className="text-sm text-gray-600">{date}</p>
      <p className="text-sm text-gray-600">{location}</p>
    </div>
  );
}
