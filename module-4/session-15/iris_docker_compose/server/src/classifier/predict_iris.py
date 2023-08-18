import logging
from pathlib import Path
import sys

# Add root to sys.path
# https://fortierq.github.io/python-import/
path_root_1 = Path(__file__).parents[1]
path_root_2 = Path(__file__).parents[2]
sys.path.append(str(path_root_1))
sys.path.append(str(path_root_2))

from iris_classifier import IrisClassifier
from src.models import Iris

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("predict_iris.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream


class PredictIris:
    def __init__(self) -> None:
        pass

    def predict(self, input_data: list = [1, 2, 3, 4]) -> dict:
        """This function makes a Iris prediction.

        Parameters
        ----------
        input_data : list, optional
            The list of necessary features to make a prediction, by default [1, 2, 3, 4]

        Returns
        -------
        dict
            _description_
        """
        classifier = IrisClassifier()
        iris = Iris(
            sepal_length=input_data[0],
            sepal_width=input_data[1],
            petal_length=input_data[2],
            petal_width=input_data[3],
        )

        return classifier.classify_iris(iris)


if __name__ == "__main__":
    input_data = [3, 4, 5, 8]
    logger.debug(f"input_data: {input_data}")
    iris = PredictIris()
    logger.debug(f"prediction: {iris.predict(input_data)}")
