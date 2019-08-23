import React from 'react';

export const PredictionData = ({ prediction }) => (
  <div className="prediction">
    <h2 className="prediction__header">The prediction is:</h2>
    <p className="prediction__name">{prediction.data}</p>
    <p className="prediction__prob">
      Confidence in the prediction:
      {prediction.prob_rounded}
      %
    </p>
  </div>
);

export default PredictionData;
