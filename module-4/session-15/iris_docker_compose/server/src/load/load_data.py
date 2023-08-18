import pandas as pd
from typing import Tuple

from sklearn.datasets import load_iris


class IrisLoadData:
    """This class loads the iris data."""

    def __init__(self) -> None:
        pass

    def load_data(self) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """Init class function that load automatically
        the iris dataset.

        Returns
        -------
        Tuple [Dataframe X, Dataframe y]
            Training data and test data.
        """
        self.X, self.y = load_iris(return_X_y=True)
        return self.X, self.y
