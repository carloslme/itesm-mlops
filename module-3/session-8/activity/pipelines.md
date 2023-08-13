# Activity: Pipelines

In this activity, you will complete three Pipelines using the existing [pipelines.ipynb](pipelines.ipynb) notebook.

## Setup

### Virtual environment

Change the directory to `module-3/session-8/activity`.

1. Create a virtual environment with `Python 3.10+`
    * Create venv

        ```bash
        python3.10 -m venv venv
        ```

    * Activate the virtual environment

        ```bash
        source venv-session-9/bin/activate
        ```

2. Install libraries
    Run the following command to install the other libraries.

    ```bash
    pip install -r requirements.txt
    ```

## Modifications

Complete the following code in the notebook:

* `numeric_pipeline`:
    This pipeline handles the numeric features in the dataset. It consists of three steps:

  * selector: Selects specific numeric columns from the input data.
  * imputer: Imputes missing values using the most frequent value in each column.
  * scaler: Scales the numeric features using standardization, ensuring they have similar ranges.

    ```python
    numeric_pipeline = Pipeline([
        # TODO: Add here the DataFrameSelector, MostFrequentImputer and StandardScaler
        ('selector', `ADD HERE YOUR CODE`),
        ('imputer', `ADD HERE YOUR CODE`),
        ('scaler', `ADD HERE YOUR CODE`)
    ])
    ```

* `categorical_pipeline`:
    This pipeline handles the categorical features in the dataset. It follows a similar structure to the numeric_pipeline:

  * selector: Selects specific categorical columns from the input data.
  * imputer: Imputes missing values using the most frequent value in each column.
  * encoder: Applies one-hot encoding to transform categorical variables into binary vectors.

    ```python
    categorical_pipeline = Pipeline([
        # TODO: Add here the DataFrameSelector, MostFrequentImputer and OneHotEncoder
        ('selector', `ADD HERE YOUR CODE`),
        ('imputer',  `ADD HERE YOUR CODE`),
        ('encoder',  `ADD HERE YOUR CODE`)
    ])
    ```

* `pipeline`:
    The `pipeline` is the main machine learning pipeline that combines all the preprocessing steps with the final classifier. It ensures that data goes through all the necessary transformations before being fed into the classifier for training and prediction.

    ```python
    pipeline = Pipeline([
        # TODO: Add here the preprocessor and a SVC trainer
        ('preprocessor', `ADD HERE YOUR CODE`),
        ('classifier', `ADD HERE YOUR CODE`)
    ])
    ```

## Output

You should see something like this:

```bash
Accuracy: 0.7786259541984732
```
