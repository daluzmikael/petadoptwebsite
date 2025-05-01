// src/components/QuestionForm.jsx
import React, { useState } from 'react';
import axios from 'axios';

function QuestionForm() {
  const [formData, setFormData] = useState({ name: '', question: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:5000/api/questions', formData)
      .then(response => {
        console.log('Question submitted:', response.data);
      })
      .catch(error => {
        console.error('Error submitting question:', error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="name"
        placeholder="Your Name"
        value={formData.name}
        onChange={handleChange}
      />
      <textarea
        name="question"
        placeholder="Your Question"
        value={formData.question}
        onChange={handleChange}
      />
      <button type="submit">Submit Question</button>
    </form>
  );
}

export default QuestionForm;
