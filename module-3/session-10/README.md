# Continuous Integration Part 2
This session is the continuation of [Session 5: Continuous Integration Part 1](../../module-2/session-5), the unit tests, border, formatting and more are addressed again. It is presented as adding GitHub Actions to validate that the code that is added to a repository has the best software development practices.

## Pytest (Unit test)
You can find the tests in the [tests](itesm_mlops/tests) folder.

### Virtual environment

1. Create a virtual environment with `Python 3.10+`
    * Create venv
        ```bash
        python3.10 -m venv venv-tests
        ```

    * Activate the virtual environment
        ```
        source venv-tests/bin/activate
        ```
    * Install the packages
        ```bash
        pip install module-3/session-10/itesm_mlops/requirements.txt
        ```


    > **NOTE**   
    Deactivate the virtual environment using this command at the end of its example.  
        ```bash
        deactivate
        ```

**The configuration is ready for the check the script!**

### Running the tests
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
