from sklearn.base import BaseEstimator, TransformerMixin


class MissingIndicator(BaseEstimator, TransformerMixin):
    """This class is a custom transformer used to identify missing
    values in a pandas dataframe.
    """

    def __init__(self, variables):
        if not isinstance(variables, list):
            self.variables = [variables]
        else:
            self.variables = variables

    def fit(self, X, y):
        return self

    def transform(self, X):
        X = X.copy()
        for var in self.variables:
            X[var + "_nan"] = X[var].isnull().astype(int)

        return X
