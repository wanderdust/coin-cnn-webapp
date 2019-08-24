#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from io import BytesIO
from PIL import Image
from model.model import make_prediction, load_model, load_cat_to_name, pretty_print_prediction
from model.image import decode_image, transform_image, image_to_tensor

# Start app
# Change default location of index.html from ./templates to ./static
app = Flask(__name__,
  static_url_path='',
  template_folder='static')

# Activate CORS.
CORS(app, resources={r'/*': {'origins': 'http://localhost:5000'}})

# Global variables
publicPath = '{}/'.format(os.getcwd())
model = load_model(publicPath + 'model/utils/checkpoint_cnn_resnet34.pth')
cat_to_name = load_cat_to_name(publicPath + 'model/utils/cat_to_name.json')



@app.route("/api/predict/", methods = ['POST'])
def root():
  image = decode_image(request.data)
  image = transform_image(image)
  image = image_to_tensor(image)

  # Instantiate the model
  prediction, prob_rounded = make_prediction(image, model, cat_to_name)
  prediction = pretty_print_prediction(prediction)

  return jsonify({'data': prediction, 'prob_rounded':prob_rounded})

# Catch all routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template('index.html')


if __name__ == '__main__':
  app.run() 