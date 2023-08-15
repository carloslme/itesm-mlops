import argparse
import joblib
import pandas as pd
import os
import sys

# Add the parent directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

from train.train_data import TitanicDataPipeline


class ModelPredictor:
    """
    A class to load a trained machine learning model and make predictions on new data.

    Parameters:
        model_path (str): Path to the trained model file (joblib format).

    Methods:
        predict(new_data):
            Makes predictions on the provided new_data using the loaded model.

    Usage:
        $ python model_predictor.py trained_models/logistic_regression_output.pkl path_to_new_data
    """

    def __init__(self, model_path):
        """
        Initializes the ModelPredictor instance.

        Parameters:
            model_path (str): Path to the trained model file (joblib format).
        """
        self.model = joblib.load(model_path)

    def predict(self, new_data):
        """
        Makes predictions on the provided new_data using the loaded model.

        Parameters:
            new_data: The data on which to make predictions.

        Returns:
            Predicted outputs from the model.
        """
        return self.model.predict(new_data)

if __name__ == "__main__":

    print(f"CUrrent dir {os.getcwd()}")
    # os.chdir('/Users/carlos/itesm-mlops/module-3/session-10/itesm_mlops/itesm_mlops')
    parser = argparse.ArgumentParser(description='Model Predictor')
    parser.add_argument('model_path', type=str, help='Path to the trained model file')
    parser.add_argument('pipeline_path', type=str, help='Path to the pipeline file')
    parser.add_argument('new_data', type=str, help='Path to the file containing new data for prediction')
    args = parser.parse_args()

    predictor = ModelPredictor(args.model_path)

    new_data = args.new_data
    import csv
    import numpy as np

    # Read CSV file
    csv_file_path = new_data  # Replace with your CSV file path
    data = []

    with open(csv_file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data.extend(iter(csv_reader))
    # Convert data to a NumPy array
    numpy_array = np.array(data)
    print(numpy_array)
    # print(new_data_preprocessed)
    # predictions = predictor.predict(new_data_preprocessed)
    # print(predictions)