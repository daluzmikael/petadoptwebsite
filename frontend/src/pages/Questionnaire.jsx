import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Questionnaire.css'; // ✅ Import the custom CSS

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
    <div className="questionnaire-page">
      <h2 className="questionnaire-title">Pet Recommendation Questionnaire</h2>
      <form onSubmit={handleSubmit} className="questionnaire-form">
        {questions.map((q, i) => (
          <div key={i}>
            <label className="questionnaire-label">{q}</label>
            <input
              type="text"
              className="questionnaire-input"
              onChange={(e) => setAnswers(prev => ({ ...prev, [i]: e.target.value }))}
              required
            />
          </div>
        ))}
        <button type="submit" className="questionnaire-submit">
          Submit
        </button>
      </form>
    </div>
  );
}
