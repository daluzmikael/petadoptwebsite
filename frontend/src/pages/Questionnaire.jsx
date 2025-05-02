import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function Questionnaire() {
  const navigate = useNavigate();
  const userId = localStorage.getItem("userId");

  useEffect(() => {
    if (!userId) navigate("/?error=login_required");
  }, []);

  const questions = [
    "How old are you?", "How active are you?", "Did you have pets growing up?",
    "Scared of hospitals?", "Would be tolerant?", "Compromises to illness?",
    "Financial limitation?", "Grew up in suburbia or farm?",
    "Who else do you live with?", "Work remotely?",
    "How many pets in this household?", "Height/Weight?",
    "Kids?", "Older people living with you?"
  ];

  const [responses, setResponses] = useState(
    questions.map(q => ({ question: q, answer: "" }))
  );

  const handleChange = (index, value) => {
    const updated = [...responses];
    updated[index].answer = value;
    setResponses(updated);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:5000/api/questionnaire/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, responses })
    });
    const result = await res.json();
    alert(result.message || "Submitted");
  };

  return (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-6">Pet Recommendation Questionnaire</h2>
      <form className="grid grid-cols-1 sm:grid-cols-2 gap-4" onSubmit={handleSubmit}>
        {responses.map((r, i) => (
          <div key={i}>
            <label className="block text-sm font-medium mb-1">{r.question}</label>
            <input
              type="text"
              value={r.answer}
              onChange={(e) => handleChange(i, e.target.value)}
              className="w-full border p-2"
              required
            />
          </div>
        ))}
        <div className="col-span-full text-center mt-6">
          <button type="submit" className="bg-green-600 text-white px-6 py-2 rounded hover:bg-green-700">
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
