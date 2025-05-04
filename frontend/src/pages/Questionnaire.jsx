import { useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Questionnaire() {
  const [answers, setAnswers] = useState({});
  const navigate = useNavigate();

  const questions = [
    "How old are you?", "How active are you?", "Did you have pets growing up?", "Scared of hospitals?",
    "Would be tolerant?", "Compromises to illness?", "Financial limitation?", "Grew up in suburbia or farm?",
    "Who else do you live?", "Work remotely?", "How many pets this household?", "Height/Weight?",
    "Kids?", "Older people living with you?"
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    const userId = localStorage.getItem("userId");

    fetch("http://localhost:5000/api/questionnaire", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ user_id: userId, answers })
    })
      .then(res => res.json())
      .then(data => {
        alert("Questionnaire submitted!");
        navigate("/matching");
      })
      .catch(err => console.error("Submit failed:", err));
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold mb-4">Pet Recommendation Questionnaire</h2>
      <form onSubmit={handleSubmit} className="grid grid-cols-2 gap-4">
        {questions.map((q, i) => (
          <div key={i}>
            <label className="block text-sm font-medium mb-1">{q}</label>
            <input
              type="text"
              className="w-full border p-2"
              onChange={(e) => setAnswers(prev => ({ ...prev, [i]: e.target.value }))}
              required
            />
          </div>
        ))}
        <button type="submit" className="col-span-2 mt-4 bg-blue-600 text-white px-4 py-2 rounded">
          Submit
        </button>
      </form>
    </div> 
  );
}
