import predictionReducer from '../../reducers/predictionReducer';

test('should set the default state', () => {
  const action = {
    type: '@@INIT'
  };
  const state = predictionReducer(undefined, action);

  expect(state).toEqual({
    prediction: ''
  });
});


test('should set the correct prediction', () => {
  const action = {
    type: 'SET_COIN_PREDICTION',
    prediction: '1 pound coin'
  };
  const state = predictionReducer({ prediction: 'something' }, action);

  expect(state).toEqual({
    prediction: action.prediction
  });
});
