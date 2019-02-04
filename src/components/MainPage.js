import React from 'react';
import Section from './Section';
import UploadImage from './UploadImage';
import SupportedCurrencies from './SupportedCurrencies';

export const MainPage = () => (
  <div>
    <div className="section section--basic">
      <Section component={UploadImage} />
    </div>

    <div className="section section--light-grey">
      <Section component={SupportedCurrencies} />
    </div>
  </div>
);

export default MainPage;
