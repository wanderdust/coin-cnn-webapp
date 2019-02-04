import React from 'react';
import uuid from 'uuid';
import supportedCurrencies from '../supportedCurrencies.json';

export const SupportedCurrencies = () => {
  const arraySplitter = (iterable = []) => {
    const splitIndex = Math.ceil(iterable.length / 2);
    const colOne = iterable.slice(0, splitIndex);
    const colTwo = iterable.slice(splitIndex);

    return [colOne, colTwo];
  };

  const currenciesColumns = arraySplitter(supportedCurrencies);

  return (
    <div className="currencies">
      <h2 className="currencies__title">Supported Currencies</h2>
      <div className="section-content currencies__list">
        {currenciesColumns.map((column) => {
          return (
            <div className="currencies__column" key={uuid()}>
              {column.map(currency => (
                <div key={currency}>{currency}</div>
              ))}
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default SupportedCurrencies;
