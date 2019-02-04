import React from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { startSetCoinPrediction } from '../actions/prediction';

export const UploadImage = ({ startSetCoinPrediction, imageFile }) => {
  const handleOnClick = () => {
    startSetCoinPrediction(imageFile);
  };

  return (
    <div>
      <button onClick={handleOnClick} type="button">Send Image</button>
    </div>
  );
};

UploadImage.defaultProps = {
  imageFile: ''
};

UploadImage.propTypes = {
  startSetCoinPrediction: PropTypes.func.isRequired,
  imageFile: PropTypes.oneOfType([
    PropTypes.string,
    PropTypes.number,
    PropTypes.object
  ])
};

const mapDispatchToProps = dispatch => ({
  startSetCoinPrediction: imageFile => dispatch(startSetCoinPrediction(imageFile))
});

export default connect(undefined, mapDispatchToProps)(UploadImage);
