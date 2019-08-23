import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { startSetCoinPrediction } from '../actions/prediction';
import PredictionData from './PredictionData';
import Loader from './Loader';
import ErrorMessage from './ErrorMessage';

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

      {
        !!prediction
        && prediction !== 'loading'
        && prediction !== 'error'
        && <PredictionData prediction={prediction} />
      }
      {
        prediction === 'loading'
        && <Loader />
      }
      {
        prediction === 'error'
        && <ErrorMessage errorMessage="Error while making a prediction. Try again in a few seconds or try with a different image" />
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
  ]),
  prediction: PropTypes.string.isRequired
};

const mapStateToProps = state => ({
  prediction: state.prediction.prediction
});

const mapDispatchToProps = dispatch => ({
  startSetCoinPrediction: imageFile => dispatch(startSetCoinPrediction(imageFile))
});

export default connect(mapStateToProps, mapDispatchToProps)(Predict);
