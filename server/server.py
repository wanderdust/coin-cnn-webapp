#!/usr/bin/env python
# coding: utf-8

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/predict")
def root():
  return "Hello world"

# Catch all paths
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
  return "Catching all paths"


if __name__ == '__main__':
  app.run() 


