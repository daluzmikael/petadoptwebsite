// src/pages/CreateAccount.jsx

import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function CreateAccount() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch("http://localhost:5000/api/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email, password })
    })
      .then((res) => {
        if (!res.ok) throw new Error("Failed to create account");
        return res.json();
      })
      .then(() => navigate("/"))
      .catch((err) => {
        console.error(err);
        setError("Account creation failed.");
      });
  };

  return (
    <div className="p-6 max-w-md mx-auto">
      <h2 className="text-3xl font-bold mb-6 text-center">Create Account</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block mb-1 font-medium">Username</label>
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} className="w-full border border-gray-300 p-2 rounded" required />
        </div>
        <div>
          <label className="block mb-1 font-medium">Email</label>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className="w-full border border-gray-300 p-2 rounded" required />
        </div>
        <div>
          <label className="block mb-1 font-medium">Password</label>
          <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} className="w-full border border-gray-300 p-2 rounded" required />
        </div>
        <button type="submit" className="w-full bg-green-600 text-white py-2 rounded hover:bg-green-700">Create Account</button>
        {error && <p className="text-red-600 text-sm mt-2">{error}</p>}
        <p className="mt-2 text-center text-sm">
          Already have an account? <a href="/" className="text-blue-600 underline">Log in</a>
        </p>
      </form>
    </div>
  );
}
