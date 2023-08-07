## Execute unit and integration tests
* Execute tests in the script and explain details
    ``
    $ pytest test_mi_Script.py -v
    ``

* Execute tests in the script and hide details
    ``
    $ pytest test_mi_script.py -q
    ``

* Execute all the tests within a folder
    ``
    $ pytest_carpeta/
    ``

* Execute a script test
    ``
    $ pytest_carpeta/test_mi_script.py
    ``

* Execute a single function within a script
    ``
    $ pytest_carpeta/test_mi_script.py :: test_funcion
    ``

* Execute a single function within a script with which you have a brand
    ``
    $ pytest_carpeta/test_mi_script.py -m mi_marca
    ``