import React from 'react';

export const ErrorMessage = ({ errorMessage }) => (
  <div className="error__message">
    <p>
      {errorMessage}
    </p>
  </div>
);

export default ErrorMessage;
