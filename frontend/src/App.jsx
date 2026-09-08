// src/App.jsx

import React from 'react';
import { BrowserRouter as Router, Navigate, Routes, Route, useLocation } from 'react-router-dom';

import Nav from './components/nav';

import Login from './pages/Login';
import CreateAccount from './pages/CreateAccount';
import Landing from './pages/Landing';
import Adopt from './pages/Adopt';
import Saved from './pages/Saved';
import FAQ from './pages/FAQ';
import Events from './pages/Events';
import Guide from './pages/Guide';
import Questionnaire from './pages/Questionnaire';
import Matching from './pages/Matching';

function App() {
  const location = useLocation();
  const isLoggedIn = Boolean(localStorage.getItem("userId"));
  const hideNav = location.pathname === "/" || location.pathname === "/create-account";

  const protectedPage = (page) => (
    isLoggedIn ? page : <Navigate to="/?error=login_required" replace />
  );

  return (
    <>
      {isLoggedIn && !hideNav && <Nav />}
      <div className="min-h-screen bg-white text-black font-sans">
        <Routes>
          <Route path="/" element={<Login />} />
          <Route path="/create-account" element={<CreateAccount />} />
          <Route path="/landing" element={protectedPage(<Landing />)} />
          <Route path="/adopt" element={protectedPage(<Adopt />)} />
          <Route path="/saved" element={protectedPage(<Saved />)} />
          <Route path="/faq" element={protectedPage(<FAQ />)} />
          <Route path="/events" element={protectedPage(<Events />)} />
          <Route path="/guide" element={protectedPage(<Guide />)} />
          <Route path="/questionnaire" element={protectedPage(<Questionnaire />)} />
          <Route path="/matching" element={protectedPage(<Matching />)} />
          <Route path="*" element={<Navigate to={isLoggedIn ? "/landing" : "/"} replace />} />
        </Routes>
      </div>
    </>
  );
}

export default function AppWrapper() {
  return (
    <Router>
      <App />
    </Router>
  );
}
