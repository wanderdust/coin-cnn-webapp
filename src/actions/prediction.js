import axios from 'axios';

export const setCoinPrediction = (prediction = '') => ({
  type: 'SET_COIN_PREDICTION',
  prediction
});

export const setLoadingState = () => ({
  type: 'SET_LOADING_STATE',
  prediction: 'loading'
});


export const startSetCoinPrediction = imageFile => (dispatch, getState) => {
  dispatch(setLoadingState());
  axios.post('/api/predict', imageFile, {
    headers: {
      'Content-Type': imageFile.type
    }
  }).then((response) => {
    dispatch(setCoinPrediction(response.data));
  }).catch((error) => {
    dispatch(setCoinPrediction('error'));
  });
};
