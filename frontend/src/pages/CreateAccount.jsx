import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./CreateAccount.css";
import { apiRequest } from "../api";

export default function CreateAccount() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    try {
      await apiRequest("/api/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, email, password }),
      });
      navigate("/");
    } catch (err) {
      setError(err.message || "Account creation failed.");
    }
  };

  return (
    <div className="create-account-page">
      <div className="create-account-card">
        <h2 className="create-account-title">Create Account</h2>
        <form onSubmit={handleSubmit} className="create-account-form">
          <div>
            <label className="create-account-label">Username</label>
            <input type="text" value={name} onChange={(e) => setName(e.target.value)} className="create-account-input" required />
          </div>
          <div>
            <label className="create-account-label">Email</label>
            <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className="create-account-input" required />
          </div>
          <div>
            <label className="create-account-label">Password</label>
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="create-account-input" required />
          </div>
          <button type="submit" className="create-account-button">Create Account</button>
          {error && <p className="create-account-error">{error}</p>}
          <p className="create-account-footer">
            Already have an account? <Link to="/" className="create-account-link">Log in</Link>
          </p>
        </form>
      </div>
    </div>
  );
}
