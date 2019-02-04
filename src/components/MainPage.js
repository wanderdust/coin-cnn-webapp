import React from 'react';
import Section from './Section';
import UploadImage from './UploadImage';

export const MainPage = () => (
  <div>
    <Section component={UploadImage} />
  </div>
);

export default MainPage;
