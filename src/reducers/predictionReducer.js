const defaultState = {
  prediction: ''
};

const predictionReducer = (state = defaultState, action) => {
  switch (action.type) {
    case 'SET_COIN_PREDICTION':
      return {
        ...state,
        prediction: action.prediction
      };
    default:
      return state;
  }
};

export default predictionReducer;
