// src/components/StatusBox.jsx
import React from 'react';

function StatusBox({ status, message }) {
  let statusClass = '';

  if (status === 'success') {
    statusClass = 'status-success';
  } else if (status === 'error') {
    statusClass = 'status-error';
  } else if (status === 'loading') {
    statusClass = 'status-loading';
  }

  return (
    <div className={`status-box ${statusClass}`}>
      <p>{message}</p>
    </div>
  );
}

export default StatusBox;
