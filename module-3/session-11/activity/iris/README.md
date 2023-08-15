# Iris Fast API

In this activity, you will have to analyze how the Iris Dataset is used in the [notebook](iris_flower.ipynb) and then migrate the code to the API created with FastAPI.

You can use the existing template in [v1](./iris/v1) folder.

## Data

The Iris dataset is a simple, yet popular dataset consisting of 150 observations. Each observation captures the sepal length, sepal width, petal length, petal width of an iris (all in cm) and the corresponding iris subclass (one of *setosa, versicolor, virginica*).

![](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

## Setup

* Create a virtual environment with:

```bash
python3 -m venv venv
```

* Activate the virtual environment

```bash
source venv/bin/activate
```

## Install the other libraries

Run the following command to install the other libraries.

```bash
pip install -r requirements.txt
```

## Usage

### Run FastAPI

Run the next command to start the app locally

```bash
uvicorn iris.v1.app:app --port 5001 --reload
```

## Activity

Modify the following files to be able to run the model.

1. Modify [app.py](iris/v1/app.py)#L14
2. Modify [iris_classifier](iris/v1/iris_classifier.py)#L18, #L19, #L23, #L24
3. Modify [models.py](iris/v1/models.py)#L7

### Test request

Once you have fixed the code, you can test it with JSON with the following fields:

* sepal_l
* sepal_w
* petal_l
* petal_w

Corresponding values are the measurements in cm.

Example request:

```bash
curl 'http://localhost:8080/v1/iris/classify_iris' -X POST -H 'Content-Type: application/json' -d '{"sepal_l": 5, "sepal_w": 2, "petal_l": 3, "petal_w": 4}'
```
