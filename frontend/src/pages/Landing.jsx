// src/pages/Landing.jsx
export default function Landing() {
    return (
      <div className="text-center">
        <h1 className="text-3xl font-bold">Pet Adoption Website</h1>
        <div className="mt-4">
          <input className="block border p-2 mx-auto mb-2" type="text" placeholder="Username" />
          <input className="block border p-2 mx-auto mb-2" type="password" placeholder="Password" />
          <button className="bg-blue-500 text-white px-4 py-2">Log In</button>
          <p className="mt-2">Not a member? <button className="underline">Sign Up</button></p>
        </div>
      </div>
    );
  }
