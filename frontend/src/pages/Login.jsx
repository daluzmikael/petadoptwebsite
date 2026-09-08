import { useState } from 'react';
import { Link, useNavigate, useLocation } from 'react-router-dom';
import './Login.css';
import { apiRequest } from '../api';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError('');

    try {
      const data = await apiRequest("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      });
      localStorage.setItem("userEmail", data.user.email);
      localStorage.setItem("userId", data.user.id);
      navigate("/landing");
    } catch (err) {
      setError(err.message || "Login failed. Make sure the backend is running.");
    }
  };

  const loginRedirectMsg = new URLSearchParams(location.search).get("error") === "login_required"
    ? "Please log in to continue."
    : "";

  return (
    <div className="login-page">
      <div className="login-card">
        <h2 className="login-title">Pet Adoption Log In</h2>
        {loginRedirectMsg && (
          <p className="login-warning">{loginRedirectMsg}</p>
        )}
        <form onSubmit={handleLogin} className="login-form">
          <div>
            <label className="login-label">Email Address</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              className="login-input"
              placeholder="example@example.com"
              required
            />
          </div>
          <div>
            <label className="login-label">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="login-input"
              placeholder="••••••••"
              required
            />
          </div>
          <button type="submit" className="login-button">Log In</button>
          {error && <p className="login-error">{error}</p>}
          <p className="login-footer">
            Don’t have an account? <Link to="/create-account" className="login-link">Create one</Link>
          </p>
        </form>
      </div>
    </div>
  );
}
