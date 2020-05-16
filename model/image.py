from PIL import Image
import numpy as np
from io import BytesIO
from keras.preprocessing.image import ImageDataGenerator

class Image_Decoder:

    def decode(self, image):
        image_pil = self.decode_image(image)
        np_image = self.transform_image(image_pil)
        img_tensor = self.image_to_tensor(np_image)
        img_norm = self.normalise(img_tensor)

        return img_norm

    # Decode from text to image
    def decode_image(self, image):
        data = BytesIO(image)
        image_pil = Image.open(data)

        return image_pil

    # Add transformations
    def transform_image(self, image):
        # Resize image
        width, height = image.size
        if width > height:
            image.thumbnail((1e10, 256))
        else:
            image.thumbnail((256, 1e10))
        
        # Crop image
        image = image.resize((224, 224))
        
        # Convert to numpy and normalize
        np_image = np.array(image)/255


        return np_image

    def image_to_tensor(self, image):
        # Transpose for image to have the correct dimensions, depth first.
        return np.expand_dims(image, axis=0)

    def normalise(self, img):

        generator = ImageDataGenerator(
            featurewise_std_normalization=True,
            samplewise_std_normalization=True,
            rescale=1./255)
        image_flow = generator.flow(
            img,
            y=None,
            batch_size=1
        )

        return image_flow.next()