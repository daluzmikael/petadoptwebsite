// src/pages/Landing.jsx

import { Link } from 'react-router-dom';

export default function Landing() {
  const email = localStorage.getItem("userEmail");

  return (
    <div className="text-center p-6">
      <h1 className="text-4xl font-bold mb-4">Welcome to the Pet Adoption Portal</h1>
      <p className="text-lg mb-6">Logged in as <strong>{email}</strong></p>

      <div className="flex justify-center gap-4 flex-wrap">
        <Link to="/adopt" className="bg-blue-500 text-white px-6 py-3 rounded hover:bg-blue-600">Adopt Pets</Link>
        <Link to="/saved" className="bg-green-500 text-white px-6 py-3 rounded hover:bg-green-600">Saved Pets</Link>
        <Link to="/guide" className="bg-purple-500 text-white px-6 py-3 rounded hover:bg-purple-600">Care Guide</Link>
        <Link to="/events" className="bg-yellow-500 text-white px-6 py-3 rounded hover:bg-yellow-600">Events</Link>
      </div>
    </div>
  );
}
