import './FAQ.css';

export default function FAQ() {
  const questions = [
    {
      question: "How do I adopt a pet?",
      answer: "Visit the Adopt page, browse pets, and click 'Adopt' to start the process."
    },
    {
      question: "What is the adoption fee?",
      answer: "Adoption fees vary by pet but usually range from $50–$200 depending on breed and age."
    },
    {
      question: "Are pets vaccinated?",
      answer: "Yes, all pets are vaccinated and medically cleared before adoption."
    },
    {
      question: "Can I return a pet after adoption?",
      answer: "Yes, we offer a 30-day return policy for all adoptions, no questions asked."
    },
    {
      question: "Where can I learn about caring for a new pet?",
      answer: "Check out our Guide section for tips on feeding, training, and vet visits."
    }
  ];

  return (
    <div className="faq-page">
      <h2 className="faq-title">Frequently Asked Questions</h2>
      <div className="faq-grid">
        {questions.map((q, index) => (
          <div key={index} className="faq-item">
            <h3 className="faq-question">{q.question}</h3>
            <p className="faq-answer">{q.answer}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
