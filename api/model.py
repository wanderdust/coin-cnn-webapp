#!/usr/bin/env python
# coding: utf-8

# This module is in charge of taking an image and making a prediction.

import torch
import PIL
from PIL import Image
import numpy as np
from torchvision import models
import os
import json
from io import BytesIO

publicPath = '{}/'.format(os.getcwd()) 

# Load the names corresponding to the labels
with open(publicPath + 'api/cat_to_name.json', 'r') as f:
  cat_to_name = json.load(f)
    
# Load the model from a saved checkpoint
def load_model(filepath):
  checkpoint = torch.load(filepath)
  model = models.resnet152(pretrained=False)
      
  model.fc = checkpoint['fc']
  model.load_state_dict(checkpoint['state_dict'])
  model.class_to_idx = checkpoint['class_to_idx']

  return model


my_model = load_model(publicPath + 'api/checkpoint_cnn_resnet152.pth').to('cpu')


def process_image (image):
  data = BytesIO(image)
  image_pil = Image.open(data)
  width, height = image_pil.size
  if width > height:
      image_pil.thumbnail((np.Inf, 256))
  else:
      image_pil.thumbnail((256, np.Inf))
  
  # Crop image
  image_pil = image_pil.resize((224, 224))
  
  # Convert to numpy and normalize
  np_image = np.array(image_pil)/255

  # mean = [0.2972239085211309 , 0.24976049135203868, 0.28533308036347665]
  # std = [0.2972239085211309, 0.24976049135203868, 0.28533308036347665]
                                          
  mean = [0.485, 0.456, 0.406]
  std = [0.229, 0.224, 0.225]

  np_image = (np_image - mean)/std
  
  # Transpose for image to have the correct dimensions, depth first.
  np_image = np_image.transpose(2, 0, 1)
  
  # Convert to tensor
  tensor_image = torch.from_numpy(np_image).float()
  
  return tensor_image


def predict(image, model, topk=5):
  model.eval()
  
  # Load the image
  image = image.unsqueeze(0)

  # Forward pass.
  output = model.forward(image)
  # Get the top element
  top_prob, top_class = torch.topk(output, topk)
  
  # Get the probabilities
  top_prob = top_prob.exp()
  
  # Convert to arrays.
  top_prob = top_prob.squeeze().detach().numpy()
  top_class = top_class.squeeze().detach().numpy()
  
  idx_to_class = {val: key for key, val in model.class_to_idx.items()}
  
  # Get the prediction with the most likelyhood
  top_class = idx_to_class[top_class[0]]
  
  return top_prob, top_class

def get_coin_name (model, top_class):
  coin_name = cat_to_name[str(top_class)]
  
  return coin_name