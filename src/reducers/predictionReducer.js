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
    case 'SET_LOADING_STATE':
      return {
        ...state,
        prediction: 'loading'
      };
    default:
      return state;
  }
};

export default predictionReducer;
