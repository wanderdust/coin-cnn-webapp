import torch
import os
from model.utils.resnet import resnet34
import json

# Load the model from a saved checkpoint
def load_model(filepath):
    '''
        model.fc -> The (personalized) fully connected layers
        model.load_sate_dict -> The trained weights
        model.class_to_idx -> The index for each class
    '''

    checkpoint = torch.load(filepath, map_location='cpu')
    model = resnet34(pretrained=False)

    model.fc = checkpoint['fc']
    model.load_state_dict(checkpoint['state_dict'])
    model.class_to_idx = checkpoint['class_to_idx']

    return model


# Load the names corresponding to the labels
def load_cat_to_name(filepath):
    with open(filepath, 'r') as f:
        cat_to_name = json.load(f)

    return cat_to_name


def predict(image, model):
    model.eval()

    # Load the image
    image = image.unsqueeze(0)

    # Forward pass.
    output = model.forward(image)

    return output


# Recieves an output and returns the class name and probability
def decode_predictions(model, output, classes):
    
    # Extract results; linear_probs gives non-useful probability results
    num_classes = len(classes)
    linear_probs, classes = torch.topk(output, num_classes)

    # Get the probabilities from in a range [0-1]
    sm = torch.nn.Softmax(dim=1)
    probs = sm(linear_probs)

    # Convert to arrays.
    top_prob = probs.squeeze().detach().numpy()
    top_class = classes.squeeze().detach().numpy()

    # Get the right indices
    idx_to_class = {val: key for key, val in model.class_to_idx.items()}

    # Get the top class and its probability
    top_class = idx_to_class[top_class[0]]
    top_prob = top_prob[0]

    return top_prob, top_class


def get_coin_name (top_class, cat_to_name):
    coin_name = cat_to_name[str(top_class)]
    
    return coin_name


def make_prediction(image, model, classes):
    output = predict(image, model)
    top_prob, top_class = decode_predictions(model, output, classes)

    prediction = get_coin_name(top_class, classes)
    prob_rounded = '{0:.2f}'.format(top_prob*100)

    return prediction, prob_rounded

