# Iris Docker Compose

This is an example of how to refactor a machine-learning model from a notebook to a production-ready code in Docker Compose.

## Considerations

* The directory structure, where data transformations (if any), training, predictions, among other things, are separated.
* Modularization of code using Object Oriented Programming.
* Refactoring of functions to avoid duplication in actions.
* Optimization of actions to make the project faster and more efficient.
* Annotations to improve the reading of the code.
* Docstrings to document the code.
* Integration of logs (Logging) to record what happens in the project.
* Add unit tests.
* Add file ***.gitignore***
* Add file ***requirements.txt*** with a list of dependencies
* Add a ***README.md*** file to the project.

## Data

The Iris dataset is a simple, yet popular dataset consisting of 150 observations. Each observation captures the sepal length, sepal width, petal length, petal width of an iris (all in cm) and the corresponding iris subclass (one of *setosa, versicolor, virginica*).

![](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Machine+Learning+R/iris-machinelearning.png)

# Setup

## Clone the project

* Just open your terminal, go or create a directory, and run the following command:

```
cd module-4/session-15/iris_docker_compose
```

> NOTE  
It is recommended to create a new directory and copy there all the code in this folder.

## Create virtual environment

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

# Usage

## Run unit tests

* Open the terminal, and run

```bash
pytest tests/unit/test_classification_response.py -v
```

You should see something like this:

```bash
(venv) carloslme@192 iris-docker-compose % pytest tests/unit/test_classification_response.py -v     
===================================================================================== test session starts =====================================================================================
platform darwin -- Python 3.7.9, pytest-7.2.0, pluggy-1.0.0 -- /Users/carloslme/Documents/iris-docker-compose/venv/bin/python3
cachedir: .pytest_cache
rootdir: /Users/carloslme/Documents/iris-docker-compose
collected 2 items                                                                                                                                                                             

tests/unit/test_classification_response.py::test_response_parametrize[4-6-5-7-virginica-1.0] PASSED                                                                                     [ 50%]
tests/unit/test_classification_response.py::test_response_parametrize[1-2-3-4-virginica-0.96] PASSED                                                                                    [100%]

====================================================================================== 2 passed in 1.45s ======================================================================================
```

## Build Docker image individually

* Run next command to build de docker image with the app.

```bash
 docker build . -t IMAGE_NAME
```

* Then, run this comand to run the image in a container.

```bash
docker run -d --name app -p 3000:3000 myimage
```

* Check logs

```bash
docker logs -f CONTAINER_ID | grep "Debug" 
```

* Delete all images

```bash
docker rmi -f $(docker images -aq)
```

* Delete all containers

```bash
docker rm -f $(docker ps -aq)  
```

## Create the network

First, create the network AIService by running this command:

```bash
docker network create AIservice
```

## Run Docker Compose

* Be sure you are un the directory where the docker-compose.yml file is located

* Run next command to start the Server and Frontend APIs

```bash
docker-compose up --build
```

You will see something like this:

```bash
Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
Creating iris-api-dev_server_1 ... done
Creating iris-api-dev_frontend_1 ... done
Attaching to iris-api-dev_server_1, iris-api-dev_frontend_1
server_1    | INFO:     Will watch for changes in these directories: ['/app']
server_1    | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
server_1    | INFO:     Started reloader process [1] using StatReload
frontend_1  | INFO:     Will watch for changes in these directories: ['/app']
frontend_1  | INFO:     Uvicorn running on http://0.0.0.0:3000 (Press CTRL+C to quit)
frontend_1  | INFO:     Started reloader process [1] using StatReload
frontend_1  | INFO:     Started server process [9]
frontend_1  | INFO:     Waiting for application startup.
frontend_1  | INFO:     Application startup complete.
server_1    | INFO:     Started server process [8]
server_1    | INFO:     Waiting for application startup.
server_1    | INFO:     Application startup complete.
```

## Test request

The input is a JSON with the following fields:

* sepal_length
* sepal_width
* petal_length
* petal_width

Corresponding values are the measurements in cm.

### CURL request

```bash
curl 'http://localhost:3000/iris/classify_iris' -X POST -H 'Content-Type: application/json' -d '{"sepal_length": 5, "sepal_width": 2, "petal_length": 3, "petal_width": 4}'
```

### FastAPI UI request

* Go to the <http://localhost:3000/docs>, and in the POST request body `/v1/classify` copy this:

```bash
{"sepal_length": 5, "sepal_width": 2, "petal_length": 3, "petal_width": 4}
```

You will get a response body like this:

```bash
{
  "response": "{\"class\":\"virginica\",\"probability\":0.91}"
}
```

# Check logs

## Extract logs

* Open a new terminal, and change the working directory where the `docker-compose.yml` is located.

* Run the following code to identify the `CONTAINER ID` of the Server container.

```bash
docker ps -a
```

You will get something like this

```bash
CONTAINER ID   IMAGE                   COMMAND                  CREATED        STATUS        PORTS                    NAMES
bd1d9305d2d0   iris-api-dev_frontend   "uvicorn main:app --…"   12 hours ago   Up 12 hours   0.0.0.0:3000->3000/tcp   iris-api-dev_frontend_1
568ee652e7e1   iris-api-dev_server     "uvicorn main:app --…"   12 hours ago   Up 12 hours   0.0.0.0:8000->8000/tcp   iris-api-dev_server_1
```

* To extract the logs, you can copy them to your local machine by running this command.

```bash
docker cp 568ee652e7e1:/app/server.log .
```

You can check the logs.log file in your local directory.
