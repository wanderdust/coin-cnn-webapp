import React from 'react';

export const PredictionData = ({ prediction }) => (
  <div className="prediction">
    <h2 className="prediction__header">The prediction is:</h2>
    <div className="prediction__data">
      <p>
        <b>Coin:</b>
        {prediction.data.coin}
      </p>
      <p>
        <b>Currency:</b>
        {prediction.data.currency}
      </p>
      <p>
        <b>Country:</b>
        {prediction.data.country}
      </p>
      <p className="prediction__prob">
        <b>Confidence in prediction:</b>
        {prediction.prob_rounded}
        %
      </p>
    </div>
  </div>
);

export default PredictionData;
