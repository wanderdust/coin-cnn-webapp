import os
import json
import numpy as np
import tensorflow as tf
import keras
from keras.models import Sequential, Model, load_model
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, GlobalAveragePooling2D

session = tf.Session(graph=tf.Graph())    
    
class Model:

    def __init__(self, int_to_dir_path, cat_to_name_path):
        self.int_to_dir = self.load_json(int_to_dir_path)
        self.cat_to_name = self.load_json(cat_to_name_path)
        self.model = self.load_model()

    def run(self, img):
        prediction, prob = self.predict(img)
        output = self.pretty_print_prediction(prediction, prob)

        return output, prob


    # Load the names corresponding to the labels
    def load_json(self, filepath):
        with open(filepath, 'r') as f:
            my_json = json.load(f)
        return my_json


    # Load the model from a saved checkpoint
    def load_model(self):
        with session.graph.as_default():
            keras.backend.set_session(session)
            model = load_model("model/utils/mobilenet.h5")
        #model.load_weights("model/utils/mobilenet.weights.best.hdf5")

        print("**Ready**")
        return model

    def predict(self, image_tensor):
        with session.graph.as_default():
            keras.backend.set_session(session)
            prediction = self.model.predict(image_tensor)
        prediction_int = np.argmax(prediction)

        prediction_prob = np.squeeze(np.array(prediction))[prediction_int]

        dir_int = self.int_to_dir[str(prediction_int)]
        label_name = self.cat_to_name[str(dir_int)]

        return label_name, prediction_prob
        

    # Takes the prediction in csv format and returns a nice object
    def pretty_print_prediction(self, prediction, prob):
        split_pred = prediction.split(',')

        coin, currency, country = split_pred

        if prob >= 0.7:
            confidence = "high"
        elif prob < 0.7 and prob >= 0.5:
            confidence = "medium"
        else:
            confidence = "low"

        prediction_dict = {
            "coin": coin,
            "currency": currency,
            "country": country,
            "prob_rounded": str(prob),
            "confidence": confidence
            }
        
        return prediction_dict