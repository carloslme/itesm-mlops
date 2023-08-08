#!/usr/bin/env python

"""Tests for `itesm_mlops` package."""
import os
import pytest
import pandas as pd

from sklearn.pipeline import Pipeline

from itesm_mlops.load.load_data import DataRetriever
from itesm_mlops.preprocess.preprocess_data import MissingIndicator

def test_missing_indicator_transform():
    """
    Test the `transform` method of the MissingIndicator transformer.

    This test checks if the transformer correctly adds indicator features for missing values
    in the specified variables and returns the modified DataFrame.

    The test case uses a sample DataFrame with missing values and a custom transformer instance.

    It checks if the transformer successfully adds indicator features for the specified variables,
    and the transformed DataFrame has the expected additional columns.

    Note: Make sure to replace 'your_module' with the actual module name where the MissingIndicator class is defined.
    """
    # Sample DataFrame with missing values
    data = {
        'age': [25, 30, None, 40],
        'income': [50000, None, 75000, 60000],
        'gender': ['M', 'F', 'M', 'F']
    }
    df = pd.DataFrame(data)

    # Instantiate the custom transformer with specified variables
    missing_indicator = MissingIndicator(variables=['age', 'income'])

    # Transform the DataFrame using the custom transformer
    df_transformed = missing_indicator.transform(df)

    # Check if the transformed DataFrame has the expected additional columns
    expected_columns = ['age_nan', 'income_nan', 'gender']
    assert all(col in df_transformed.columns for col in expected_columns), \
        f"The transformed DataFrame should have the following additional columns: {expected_columns}"

    # Check if the values in the added indicator columns are correct
    expected_values = [0, 1, 0, 0]
    assert all(df_transformed['age_nan'] == expected_values), \
        f"Expected values for 'age_nan': {expected_values}"

    expected_values = [0, 1, 0, 0]
    assert all(df_transformed['income_nan'] == expected_values), \
        f"Expected values for 'income_nan': {expected_values}"

    # Check if the original DataFrame is not modified
    assert 'age_nan' not in df.columns, "The original DataFrame should not be modified."

def test_missing_indicator_fit():
    """
    Test the `fit` method of the MissingIndicator transformer.

    This test checks if the `fit` method returns the transformer instance itself,
    without performing any actual training or fitting.

    The test case uses a sample DataFrame and a custom transformer instance.

    Note: Make sure to replace 'your_module' with the actual module name where the MissingIndicator class is defined.
    """
    # Sample DataFrame
    data = {
        'age': [25, 30, 35, 40],
        'income': [50000, 60000, 75000, 80000],
        'gender': ['M', 'F', 'M', 'F']
    }
    df = pd.DataFrame(data)

    # Instantiate the custom transformer without specifying variables
    missing_indicator = MissingIndicator()

    # Fit the transformer to the DataFrame
    transformer_instance = missing_indicator.fit(df)

    # Check if the fit method returns the transformer instance itself
    assert transformer_instance == missing_indicator, \
        "The `fit` method should return the transformer instance itself."


def does_csv_file_exist(file_path):
    """
    Check if a CSV file exists at the specified path.

    Parameters:
        file_path (str): The path to the CSV file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    return os.path.isfile(file_path)

def test_csv_file_existence():
    """
    Test case to check if the CSV file exists.
    """
    # Provide the path to your CSV file that needs to be tested
    os.chdir('/Users/carlos/itesm-mlops/module-3/session-10/itesm_mlops/itesm_mlops')
    csv_file_path = "./data/retrieved_data.csv"
    
    DATASETS_DIR = './data/'
    
    URL = 'https://www.openml.org/data/get_csv/16826755/phpMYEkMl'
    data_retriever = DataRetriever(URL, DATASETS_DIR)
    data_retriever.retrieve_data()

    # Call the function to check if the CSV file exists
    file_exists = does_csv_file_exist(csv_file_path)

    # Use Pytest's assert statement to check if the file exists
    assert file_exists == True, f"The CSV file at '{csv_file_path}' does not exist."

if __name__ == "__main__":
    # Run the test function using Pytest
    pytest.main([__file__])

