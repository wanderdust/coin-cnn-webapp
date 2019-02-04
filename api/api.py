#!/usr/bin/env python
# coding: utf-8

from flask import Flask
from flask import jsonify
import model

app = Flask(__name__)

@app.route("/api/predict/")
def root():
  my_model = model.my_model
  image = model.process_image('/home/pablo/Desktop/stuff/coin_cnn/data/test/132/031__10 Rupees_pakistan.jpg')
  _, classes = model.predict(image, my_model)
  prediction = model.get_coin_name(my_model, classes)

  return jsonify(prediction)


if __name__ == '__main__':
  app.run()