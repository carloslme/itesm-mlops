# REST API

This session is focused on giving an introduction to Rest API and the Fastapi Framework. It is explained how to migrate a project already referred to as a Rest API.

## Setup

* Change the directory to the `module-3/session-11/itesm_mlops/itesm_mlops` folder.

* Create a virtual environment with Python 3+:

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

## Running tests

The following test validates the [load_data.py](itesm_mlops/itesm_mlops/load/load_data.py) module, with the `DataRetriever` class.

Follow the next steps to run the test.

* Change the directory and run the following command:

    ```bash
    cd session-10/itesm_mlops/
    ```

* Then run:

    ```bash
    pytest ./tests/test_itesm_mlops.py::test_csv_file_existence -v
    ```

* You should see the following data output:

    ```pytest
    ================================================ test session starts =================================================
    platform darwin -- Python 3.10.12, pytest-7.4.0, pluggy-1.2.0 -- /Users/carlos/itesm-mlops/module-3/session-10/itesm_mlops/venv-tests/bin/python3.10
    cachedir: .pytest_cache
    rootdir: /Users/carlos/itesm-mlops/module-3/session-10/itesm_mlops
    collected 1 item                                                                                                     

    tests/test_itesm_mlops.py::test_csv_file_existence PASSED                                                      [100%]

    ================================================= 1 passed in 2.85s ==================================================
    ```

## Run FastAPI

* Run the next command to start the Titanic API locally

    ```bash
    uvicorn api.main:app --reload
    ```

## Checking endpoints

1. Access `http://127.0.0.1:8000/`, you will see a message like this `"Titanic is all ready to go!"`
2. Access `http://127.0.0.1:8000/docs`, the browser will display something like this:
    ![FastAPI Docs](itesm_mlops/docs/imgs/fast-api-docs.png)
3. Try running the following predictions with the endpoint by writing the following values:
    * **Prediction 1**  
        Request body

        ```bash
        {
        "pclass_nan": 0,
        "age_nan": 0,
        "sibsp_nan": 0,
        "parch_nan": 0,
        "fare_nan": 0,
        "sex_male": 1,
        "cabin_Missing": 1,
        "cabin_rare": 0,
        "embarked_Q": 1,
        "embarked_S": 0,
        "title_Mr": 1,
        "title_Mrs": 0,
        "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [0]"
        ```

    * **Prediction 2**  
        Request body

        ```bash
         {
            "pclass_nan": 0,
            "age_nan": 0,
            "sibsp_nan": 1,
            "parch_nan": 0,
            "fare_nan": 0,
            "sex_male": 0,
            "cabin_Missing": 0,
            "cabin_rare": 0,
            "embarked_Q": 1,
            "embarked_S": 0,
            "title_Mr": 1,
            "title_Mrs": 0,
            "title_rar": 0
        }
        ```

        Response body
        The output will be:

        ```bash
        "Resultado predicción: [1]"
        ```
