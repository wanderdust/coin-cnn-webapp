import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { startSetCoinPrediction } from '../actions/prediction';

export const Predict = ({ startSetCoinPrediction, imageFile, prediction }) => {
  const handleOnClick = () => {
    startSetCoinPrediction(imageFile);
  };

  return (
    <div className="predict">
      <button
        onClick={handleOnClick}
        type="button"
        disabled={!imageFile}
        className={`button ${!imageFile && 'button--disabled'}`}
      >
        Make Prediction
      </button>

      {!!prediction && 
        (
          <div>
            <h2>The prediction is:</h2>
            <p>{prediction}</p>
          </div>
        )
      }
    </div>
  );
};

Predict.defaultProps = {
  imageFile: ''
};

Predict.propTypes = {
  startSetCoinPrediction: PropTypes.func.isRequired,
  imageFile: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number,
    PropTypes.object
  ])
};

const mapStateToProps = state => ({
  prediction: state.prediction.prediction
});

const mapDispatchToProps = dispatch => ({
  startSetCoinPrediction: imageFile => dispatch(startSetCoinPrediction(imageFile))
});

export default connect(mapStateToProps, mapDispatchToProps)(Predict);
