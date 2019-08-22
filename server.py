#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from io import BytesIO
from PIL import Image

# Start app
# Change default location of index.html from ./templates to ./static
app = Flask(__name__,
  static_url_path='',
  template_folder='static')

# Activate CORS.
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/api/predict/", methods = ['POST'])
def root():
  img = request.data

  return "hello world"

# Catch all routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return render_template('index.html')


if __name__ == '__main__':
  app.run() 