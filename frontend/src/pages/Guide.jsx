// src/pages/Guide.jsx
// src/pages/Guide.jsx

export default function Guide() {
  const categories = ["Dog", "Cat", "Equine", "Rodent", "Reptile", "Bird"];

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6">Pet Supply and Care Guide</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {categories.map((type) => (
          <div key={type} className="border rounded shadow overflow-hidden bg-white">
            <img
              src={`/${type.toLowerCase()}.jpg`}
              alt={`${type} Care`}
              className="w-full h-32 object-cover rounded-t"
            />
            <div className="p-4 text-center">
              <p className="font-semibold text-lg">{type} Care</p>
              <ul className="text-sm mt-2 space-y-1 text-gray-700 text-left">
                <li>• General</li>
                <li>• Supplies</li>
                <li>• Training</li>
                <li>• Medical</li>
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
