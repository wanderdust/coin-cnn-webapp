from PIL import Image
import numpy as np
from io import BytesIO

class Image_Decoder:

    def decode(self, image):
        image_pil = self.decode_image(image)
        np_image = self.transform_image(image_pil)
        img_tensor = self.image_to_tensor(np_image)

        return img_tensor

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

        # Normalize
        mean = [0.485, 0.456, 0.406]
        std = [0.229, 0.224, 0.225]
        img = (img - mean)/std

        return np_image

    def image_to_tensor(self, image):
        # Transpose for image to have the correct dimensions, depth first.
        return np.expand_dims(image, axis=0)

    def unormalize_image(np_image):
        # Undo preprocessing
        mean = np.array([0.485, 0.456, 0.406])
        std = np.array([0.229, 0.224, 0.225])
        image = std * image + mean

        return image