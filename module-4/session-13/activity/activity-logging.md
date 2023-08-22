# Activity Logging

In this activity, you will use this [logging-advanced.ipynb](logging-advanced.ipynb) notebook with more advanced features that the Logging built-in dependency has. Please check the section `Configuring one Log file` to run the cells and understand the flow.

## Task

Modify the [demo_fast_api_logging](../demo_fast_api_logging) to meet the requirements below:

* Include a logger called `calculator.log` in the [calculator.py](../demo_fast_api_logging/src/calculator/calculator.py) module.
* The logger should have configured the `DEBUG` level.
* Include a logging exception for the function `divide` method when the divison is executed by zero.
* Add a `logging.StreamHandler()` to visualize them also on console.

>**NOTE**  
Check the [logging-advanced.ipynb](logging-advanced.ipynb) notebook to see how to add the `StreamHandler`.

## Extra

* Create a folder called `utilities` in the root directory `demo_fast_api_logging`.

* Create a `CustomLogging` class that can be instantiated and allow to create a logger instead of writing all the following lines:

    ```python
    import logging

    logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
    logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

    formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

    file_handler = logging.FileHandler('employee.log') # Indicamos el nombre del archivo

    file_handler.setFormatter(formatter) # Configuramos el formato

    logger.addHandler(file_handler) # Agregamos el archivo
    ```

* Replace the logger in the [main.py](../demo_fast_api_logging/src/main.py) module by a instance of your class.

* Then, replace the logger in the [calculator.py](../demo_fast_api_logging/src/calculator/calculator.py) module by a instance of your class.

* The directory structure should be seen as follows:

    ```bash
    my-project
    ├── api
    │   ├── main.py
    │   └── models
    ├── other-directories
    └── utilities
        ├── __init__.py
        └── custom_logging.py
    ```
