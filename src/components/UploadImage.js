import React, { useState } from 'react';
import ImageUploader from 'react-images-upload';
import Predict from './Predict';

export const UploadImage = () => {
  const [image, setImage] = useState('');

  const onChange = (data) => {
    setImage(data[0]);
  };

  return (
    <div>
      <ImageUploader
        withIcon={false}
        withPreview={true}
        buttonText="Choose images"
        imgExtension={['.jpg', '.png']}
        onChange={onChange}
        singleImage={true}
      />

      <Predict imageFile={image} />
    </div>
  );
};


export default UploadImage;
