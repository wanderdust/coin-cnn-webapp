import PIL
from PIL import Image
import numpy as np
from io import BytesIO
import torch

# Decode from text to image
def decode_image(image):
    data = BytesIO(image)
    image_pil = Image.open(data)

    return image_pil

# Add transformations
def transform_image(image):
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

    # mean = [0.2972239085211309 , 0.24976049135203868, 0.28533308036347665]
    # std = [0.2972239085211309, 0.24976049135203868, 0.28533308036347665]
                                            
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]

    np_image = (np_image - mean)/std

    return np_image

def image_to_tensor(image):
    # Transpose for image to have the correct dimensions, depth first.
    image = image.transpose(2, 0, 1)
    
    # Convert to tensor
    tensor_image = torch.from_numpy(image).float()
    
    return tensor_image