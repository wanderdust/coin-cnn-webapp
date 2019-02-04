import { setCoinPrediction } from '../../actions/prediction';

test('should create the correct setCoinPrediction action', () => {
  const prediction = '2 Pounds';

  expect(setCoinPrediction(prediction)).toEqual({
    type: 'SET_COIN_PREDICTION',
    prediction
  });
});
