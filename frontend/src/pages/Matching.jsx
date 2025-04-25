// src/pages/Matching.jsx
export default function Matching() {
    return (
      <div>
        <h2 className="text-2xl font-bold mb-4">Pet Compatibility Matching</h2>
        <div className="grid grid-cols-4 gap-4">
          {["Puppy Rottweiler", "Orange Kitten", "Alexandrine Parakeet", "Stallion", "Siamese Cat", "German Shepherd", "Bearded Lizard", "Hamster", "Peregrine Falcon"].map(pet => (
            <div key={pet} className="border p-2">
              <img src="/placeholder.jpg" alt={pet} className="w-full h-32 object-cover" />
              <p className="text-center mt-2">{pet}</p>
            </div>
          ))}
        </div>
      </div>
    );
  }