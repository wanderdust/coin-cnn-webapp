#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from io import BytesIO
from PIL import Image
from model.model import Model
from model.image import Image_Decoder

# Start app
# Change default location of index.html from ./templates to ./static
app = Flask(__name__,
  static_url_path='',
  template_folder='static')

# Activate CORS.
CORS(app, resources={r'/*': {'origins': 'http://localhost:5000'}})

# Global variables
publicPath = '{}/'.format(os.getcwd())

int_to_dir_path = publicPath + 'model/utils/int_to_dir.json'
cat_to_name_path = publicPath + 'model/utils/cat_to_name.json'


decoder = Image_Decoder()
model = Model(int_to_dir_path, cat_to_name_path)

@app.route("/api/predict/", methods = ['POST'])
def root():
  image = decoder.decode(request.data)
  # Instantiate the model
  prediction, prob = model.run(image)
  #prob_format = "{:.2f}".format(prob*100)
  
  return jsonify({'data': prediction, 'prob_rounded':prediction["confidence"]})

# Catch all routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template('index.html')


if __name__ == '__main__':
  app.run(threaded=False) 