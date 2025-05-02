// src/components/QuestionForm.jsx

import React, { useState } from 'react';

export default function QuestionForm() {
  const [answers, setAnswers] = useState({ q1: '', q2: '' });

  const handleChange = (e) => {
    setAnswers({ ...answers, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', answers);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block font-bold">Why do you want to adopt?</label>
        <input
          name="q1"
          value={answers.q1}
          onChange={handleChange}
          className="border p-2 w-full"
        />
      </div>
      <div>
        <label className="block font-bold">Do you have previous experience with pets?</label>
        <input
          name="q2"
          value={answers.q2}
          onChange={handleChange}
          className="border p-2 w-full"
        />
      </div>
      <div>
        <label className="block font-bold">How old are you?</label>
        <input
          name="q1"
          value={answers.q1}
          onChange={handleChange}
          className="border p-2 w-full"
        />
      </div>
      <div>
        <label className="block font-bold">Do you live in a small or big home?</label>
        <input
          name="q1"
          value={answers.q1}
          onChange={handleChange}
          className="border p-2 w-full"
        />
      </div>
      <button className="bg-green-500 text-white px-4 py-2 rounded">Submit</button>
    </form>
  );
}
