from fastapi import FastAPI
from starlette.responses import JSONResponse
from iris.v1.iris_classifier import IrisClassifier as IrisClassifier
from iris.v1.models import Iris

app = FastAPI()

@app.get('/v1/healthcheck', status_code=200)
async def healthcheck():
    return 'Iris classifier is all ready to go!'

@app.post('/v1/classify_iris')
def extract_name(iris_features: Iris):
    # TODO: Instantiate the Classifier here
    return JSONResponse(iris_classifier.classify_iris(iris_features))

