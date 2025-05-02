// src/components/petcard.jsx

export default function PetCard({ name, species, breed }) {
  return (
    <div className="border p-4 rounded shadow text-center">
      <h3 className="text-xl font-bold">{name}</h3>
      <p>{species} • {breed}</p>
      <button className="mt-2 px-4 py-1 bg-blue-500 text-white rounded">Save</button>
    </div>
  );
}
