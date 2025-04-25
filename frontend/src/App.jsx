// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Adopt from './pages/Adopt';
import Saved from './pages/Saved';
import FAQ from './pages/FAQ';
import Events from './pages/Events';
import Login from './pages/Login';
import Guide from './pages/Guide';
import Questionnaire from './pages/Questionnaire';

function App() {
  return (
    <Router>
      <Nav />
      <div className="min-h-screen bg-white text-black font-sans">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/adopt" element={<Adopt />} />
          <Route path="/saved" element={<Saved />} />
          <Route path="/faq" element={<FAQ />} />
          <Route path="/events" element={<Events />} />
          <Route path="/guide" element={<Guide />} />
          <Route path="/questionnaire" element={<Questionnaire />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

