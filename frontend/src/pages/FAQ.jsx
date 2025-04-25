// src/pages/FAQ.jsx
export default function FAQ() {
    return (
      <div>
        <h2 className="text-2xl font-bold mb-4">FAQ</h2>
        <div className="grid grid-cols-2 gap-4">
          {["Question 1", "Question 2", "Question 3", "Question 4", "Adoption Guides"].map(q => (
            <div key={q} className="border p-2">
              <h3 className="font-bold">{q}</h3>
              <p>Question heading</p>
              <p>Body</p>
            </div>
          ))}
        </div>
      </div>
    );
  }
  