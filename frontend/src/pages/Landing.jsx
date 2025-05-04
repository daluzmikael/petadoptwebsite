// src/pages/Landing.jsx

export default function Landing() {
  const email = localStorage.getItem("userEmail");

  return (
    <div className="text-center p-6">
      <h1 className="text-4xl font-bold mb-4">Welcome to the Pet Adoption Portal</h1>
      <p className="text-lg mb-6">Logged in as <strong>{email}</strong></p>


    </div>
  );
}
