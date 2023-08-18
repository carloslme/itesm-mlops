from fastapi import FastAPI
from starlette.responses import JSONResponse
import logging

from src.classifier.iris_classifier import IrisClassifier
from src.models import Iris


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(levelname)s: %(asctime)s|%(name)s|%(message)s")

file_handler = logging.FileHandler("server.log")
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)  # Se agrega handler para stream


app = FastAPI()
iris_classifier = IrisClassifier()


@app.get("/", status_code=200)
async def healthcheck():
    return "Iris classifier is all ready to go!"


@app.post("/classify_iris")
def extract_name(iris_features: Iris):
    print(type(iris_classifier))
    return JSONResponse(iris_classifier.classify_iris(iris_features))


@app.on_event("startup")
async def startup():
    iris_classifier.load_model()
