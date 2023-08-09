import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

from iris.v1.models import Iris

class IrisClassifier:
    def __init__(self):
        self.X, self.y = load_iris(return_X_y=True)
        self.clf = self.train_model()
        self.iris_type = {
            0: 'setosa',
            1: 'versicolor',
            2: 'virginica'
        }

    def train_model(self) -> LogisticRegression:
        # TODO: PUT YOUR CODE HERE
        return "THE MODEL HERE"

    def classify_iris(self, iris: Iris):
        X = [iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]    
        # TODO: Create the code to make a prediction
        # TODO: How to return a dictionary in this format `{'class': "", 'probability': ""}`
        return {}



