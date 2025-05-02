// src/pages/Login.jsx

import { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

export default function Login() {
  const [email, setEmail] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();
  const location = useLocation();

  const handleLogin = (e) => {
    e.preventDefault();

    fetch("http://localhost:5000/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email })
    })
      .then((res) => {
        console.log("Login response status:", res.status);
        return res.json();
      })
      .then((data) => {
        console.log("Login response data:", data);
        if (data.user) {
          localStorage.setItem("userEmail", data.user.email);
          localStorage.setItem("userId", data.user.id);
          navigate("/adopt");
        } else {
          setError("Login failed: user not found.");
        }
      })
      .catch((err) => {
        console.error("Login error (catch):", err);
        setError("Login failed: network or server error.");
      });
  };

  const loginRedirectMsg = new URLSearchParams(location.search).get("error") === "login_required"
    ? "Please log in to continue."
    : "";

  return (
    <div className="p-6 max-w-md mx-auto">
      <h2 className="text-3xl font-bold mb-6 text-center">Log In</h2>
      {loginRedirectMsg && (
        <p className="text-red-600 text-sm mb-4 text-center">{loginRedirectMsg}</p>
      )}
      <form onSubmit={handleLogin} className="space-y-4">
        <div>
          <label className="block mb-1 font-medium">Email Address</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full border border-gray-300 p-2 rounded"
            placeholder="example@example.com"
            required
          />
        </div>
        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded hover:bg-blue-700"
        >
          Log In
        </button>
        {error && <p className="text-red-600 text-sm mt-2">{error}</p>}
      </form>
    </div>
  );
}
