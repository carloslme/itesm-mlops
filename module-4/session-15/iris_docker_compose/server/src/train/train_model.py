import pandas as pd
from sklearn.linear_model import LogisticRegression


class IrisTrainModel:
    """This class trains the model with LogisticRegression."""

    def __init__(self) -> None:
        pass

    def train_model(self, X: pd.DataFrame, y: pd.DataFrame) -> LogisticRegression:
        """Init class function that trains the model using LogisticRegression.

        Returns
        -------
        LogisticRegression
            Logistic Regression classifier.
        """

        return LogisticRegression(
            solver="lbfgs", max_iter=1000, multi_class="multinomial"
        ).fit(X, y)
