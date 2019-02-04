#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify
from flask_cors import CORS
import model
from PIL import Image

app = Flask(__name__)
CORS(app)

@app.route("/api/predict/", methods = ['POST'])
def root():
  img = request.data
  my_model = model.my_model
  image = model.process_image(img)
  _, classes = model.predict(image, my_model)
  prediction = model.get_coin_name(my_model, classes)
  print(prediction)

  return jsonify(prediction)


if __name__ == '__main__':
  app.run()