import './Guide.css';

export default function Guide() {
  const categories = ["Dog", "Cat", "Equine", "Rodent", "Reptile", "Bird"];

  return (
    <div className="guide-page">
      <h2 className="guide-title">Pet Supply and Care Guide</h2>
      <div className="guide-grid">
        {categories.map((type) => (
          <div key={type} className="guide-card">
            <img
              src={`/${type.toLowerCase()}.jpg`}
              alt={`${type} Care`}
              className="guide-image"
            />
            <div className="guide-card-content">
              <p className="guide-card-title">{type} Care</p>
              <ul className="guide-card-list">
                <li>General</li>
                <li>Supplies</li>
                <li>Training</li>
                <li>Medical</li>
              </ul>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}