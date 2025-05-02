// src/components/nav.jsx

import { Link } from 'react-router-dom';

export default function Nav() {
  return (
    <nav className="bg-gray-800 text-white px-6 py-4">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between">
        <div className="font-bold text-xl mb-2 sm:mb-0">🐾 PetAdopt</div>
        <div className="flex flex-wrap gap-4 text-sm">
          <Link to="/" className="hover:underline">Login</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/adopt" className="hover:underline">Adopt</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/saved" className="hover:underline">Saved</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/faq" className="hover:underline">FAQ</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/events" className="hover:underline">Events</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/guide" className="hover:underline">Guide</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/questionnaire" className="hover:underline">Questionnaire</Link>
          <span style={{ fontSize: "24px", marginRight: "8px" }}>●</span>
          <Link to="/matching" className="hover:underline">Matching</Link>
        </div>
      </div>
    </nav>
  );
}

