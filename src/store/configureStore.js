import {
  createStore,
  combineReducers,
  applyMiddleware,
  compose
} from 'redux';
import thunk from 'redux-thunk';
import predictionReducer from '../reducers/predictionReducer';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

/*
* Store creation.
* We export it in a function so when we import it it gets called right away
* and it is ready to use.
*/
export default () => {
  const store = createStore(
    combineReducers({
      prediction: predictionReducer
    }),
    composeEnhancers(applyMiddleware(thunk))
  );

  return store;
};
