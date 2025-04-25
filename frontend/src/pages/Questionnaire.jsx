// src/pages/Questionnaire.jsx
export default function Questionnaire() {
    const questions = [
      "How old are you?", "How active are you?", "Did you have pets growing up?", "Scared of hospitals?", "Would be tolerant?", "Compromises to illness?",
      "Financial limitation?", "Grew up in suburbia or farm?", "Who else do you live?", "Work remotely?", "How many pets this household?", "Height/Weight?",
      "Kids?", "Older people living with you?"
    ];
  
    return (
      <div>
        <h2 className="text-2xl font-bold mb-4">Pet Recommendation Questionnaire</h2>
        <form className="grid grid-cols-2 gap-4">
          {questions.map((q, i) => (
            <div key={i}>
              <label className="block text-sm font-medium mb-1">{q}</label>
              <input type="text" className="w-full border p-2" />
            </div>
          ))}
        </form>
      </div>
    );
  }