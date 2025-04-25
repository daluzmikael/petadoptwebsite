import React from 'react';
import { Link } from 'react-router-dom';

function Landing() {
  return (
    <div>
      <h1>Welcome to PawPal</h1>
      <Link to="/adopt">Browse Pets</Link>
    </div>
  );
}

export default Landing;

