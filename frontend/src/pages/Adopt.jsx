// src/pages/Adopt.jsx
export default function Status() {
    return (
      <div>
        <h2 className="text-2xl font-bold mb-4">Application Status</h2>
        <div className="border p-4 text-center">
          <p className="text-xl font-bold">Current Status</p>
          <p className="text-lg">Pending Approval</p>
          <button className="bg-gray-300 px-4 py-1 mt-2">Current Hold</button>
          <p className="mt-2">Dog Adoption Safety Form</p>
        </div>
      </div>
    );
  }