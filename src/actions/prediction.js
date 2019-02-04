import axios from 'axios';

export const setCoinPrediction = (prediction = '') => ({
  type: 'SET_COIN_PREDICTION',
  prediction
});

export const startSetCoinPrediction = imageFile => (dispatch, getState) => (
  axios.post('http://localhost:5000/api/predict/', imageFile, {
    headers: {
      'Content-Type': imageFile.type
    }
  }).then((response) => {
    dispatch(setCoinPrediction(response.data.prediction));
    console.log(response);
  }).catch((error) => {
    dispatch(setCoinPrediction('Error while making a prediction'));
  })
);
