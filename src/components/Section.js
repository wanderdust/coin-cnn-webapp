import React from 'react';
import propTypes from 'prop-types';

export const Section = ({ component: Component }) => (
  <div className="content">
    <div className="section__content">
      <Component />
    </div>
  </div>
);

Section.propTypes = {
  component: propTypes.func.isRequired
};

export default Section;
