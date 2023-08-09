# Demo Calculator-Fast-API
In this demo, you will be able to deploy a simple calculator with 4 basic operations (+, -, * and /) using Fast API.

## Setup
* Create a virtual environment with:
    ```bash
    python3 -m venv venv
    ```

* Activate the virtual environment
    ```bash
    source venv/bin/activate
    ```

* Install the other libraries
Run the following command to install the libraries/packages.
    ```bash
    pip install -r requirements.txt
    ```

## Run FastAPI

* Change to the [demo_fast_api](.) directory
* Run next command to start calculator api locally 
    ```bash
    uvicorn src.main:app --reload
    ```

## Checking endpoints
1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Calculator is all ready to go!"`
2. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
    ![FastAPI Docs](./imgs/fast-api-docs.png)
3. Try running the sum endpoint by writing the values `3` and `5`, you will get the response body as follows
	
    **Response body**
    ```bash
    {
    "resultado": 8
    }
    ```
    ![sum](./imgs/sum.png)