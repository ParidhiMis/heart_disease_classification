import numpy as np
import pickle

with open("./model/model.pkl", "rb") as f:
    data = pickle.load(f)

w = data["w"]
b = data["b"]
mu = data["mu"]
sigma = data["sigma"]


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


def probability_function(X, w, b):
    z = np.dot(X, w) + b
    return sigmoid(z)


def predict(X, w, b):
    p = probability_function(X, w, b)
    return (p >= 0.5).astype(int)


def predict_heart(features):
    """
    features: list of 13 float values (user input)
    """
    X = np.array(features, dtype=float)

    X_norm = (X - mu) / sigma

    result = predict(X_norm, w, b)

    return int(result)
