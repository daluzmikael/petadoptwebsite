// src/pages/Guide.jsx
export default function Guide() {
    const categories = ["Dog", "Cat", "Equine", "Rodent", "Reptile", "Bird"];
    return (
      <div>
        <h2 className="text-2xl font-bold mb-4">Pet Supply and Care Guide</h2>
        <div className="grid grid-cols-3 gap-4">
          {categories.map(type => (
            <div key={type} className="text-center border p-2">
              <img src="/placeholder.jpg" alt={`${type} Care`} className="w-full h-32 object-cover" />
              <p className="font-bold mt-2">{type} Care</p>
              <ul className="text-sm">
                <li>General</li>
                <li>Supplies</li>
                <li>Training</li>
                <li>Medical</li>
              </ul>
            </div>
          ))}
        </div>
      </div>
    );
  }
  