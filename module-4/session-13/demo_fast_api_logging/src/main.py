import logging
from enum import Enum
from fastapi import (
    FastAPI, 
    Body,
    Path, 
    Query, 
    HTTPException,
    status)
from .calculator.calculator import Calculator

calc = Calculator()
logger = logging.getLogger(__name__) # Indicamos que tome el nombre del modulo
logger.setLevel(logging.DEBUG) # Configuramos el nivel de logging

formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s') # Creamos el formato

file_handler = logging.FileHandler('main_fast_api.log') # Indicamos el nombre del archivo

file_handler.setFormatter(formatter) # Configuramos el formato

logger.addHandler(file_handler) # Agregamos el archivo

class CalculatorFormat(str, Enum):
    SHORT = "digital"
    FULL = "analogic"


app = FastAPI()

"""
PARAMETER VALUES
Values are required after de endpoint.
"""


@app.get('/', status_code=200)
async def healthcheck():
    logger.info("Healthy was checked.")
    return 'Calculator is all ready to go!'


@app.get("/sum/{v1}/{v2}")
async def sum(v1: int, v2: int):
    """
    Calculate the sum of two integer values.....

    This endpoint calculates the sum of two integer values and returns the result.

    Parameters:
    - **v1**: The first integer value.
    - **v2**: The second integer value.

    Responses:
    - **200 OK**: The sum was calculated successfully.
        - Response JSON:
            ```
            {
                "resultado": int (sum of v1 and v2)
            }
            ```
    - **422 Unprocessable Entity**: Validation error.
        - Response JSON:
            ```
            {
                "detail": [
                    {
                        "loc": ["path", "v1"],
                        "msg": "value is not a valid integer",
                        "type": "type_error.integer"
                    },
                    {
                        "loc": ["path", "v2"],
                        "msg": "value is not a valid integer",
                        "type": "type_error.integer"
                    }
                ]
            }
            ```
    """
    result = int(calc.sum(v1, v2))
    print(f"'resultad sum': {result}")
    logger.debug(f"resultado sum: {result}")
    return {"resultado": result}


"""
In a REST API, query parameters are commonly used on read endpoints 
to apply pagination, a filter, a sorting order, or selecting fields.
"""


@app.get("/subtract/")
async def subtract(v1: float = 1.0, v2: float = 2.0):
    """
    Calculate the subtraction of two float values.

    This endpoint calculates the subtraction of two float values and returns the result.

    Parameters:
    - **v1**: The first float value. (Default: 1.0)
    - **v2**: The second float value. (Default: 2.0)

    Responses:
    - **200 OK**: The subtraction was calculated successfully.
        - Response JSON:
            ```
            {
                "resultado": int (subtraction of v1 and v2)
            }
            ```
    - **422 Unprocessable Entity**: Validation error.
        - Response JSON:
            ```
            {
                "detail": [
                    {
                        "loc": ["query", "v1"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    },
                    {
                        "loc": ["query", "v2"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    }
                ]
            }
            ```
    """
    result = int(calc.subtract(v1, v2))
    print(f"'resultado subtract': {result}")
    logger.debug(f"resultado subtract: {result}")
    return {"resultado": result}


@app.get("/divide/{v1}/{v2}")
async def divide(v1: float, v2: float):
    """
    Calculate the division of two float values.

    This endpoint calculates the division of two float values and returns the result.
    Division by zero is not allowed.

    Parameters:
    - **v1**: The dividend float value.
    - **v2**: The divisor float value.

    Responses:
    - **200 OK**: The division was calculated successfully.
        - Response JSON:
            ```
            {
                "resultado": int (division of v1 by v2)
            }
            ```
    - **400 Bad Request**: Division by zero or invalid input.
        - Response JSON:
            ```
            {
                "detail": "Can't divide by 0"
            }
            ```
    - **422 Unprocessable Entity**: Validation error.
        - Response JSON:
            ```
            {
                "detail": [
                    {
                        "loc": ["path", "v1"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    },
                    {
                        "loc": ["path", "v2"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    }
                ]
            }
            ```
    """
    if v2 == 0 or v1 == 0:
        print("resultado: cannot divide with 0")
        logger.debug('resultado: cannot divide with 0')
        return {"resultado": "can't divide with 0"}

    result = int(calc.divide(v1, v2))
    logger.debug(f'resultado divide: {result}')
    return {"resultado": result}


"""
Query is a class from the fastapi library. 
It's used to validate query parameters in an API call. 
It takes two arguments, default value and validation rules. 
In this case we're using gt for greater than and le for less 
than or equal to. The Query class can be used with any type 
of variable including int, str, float etc...
"""


@app.get("/divide-format")
async def divide_format(
    format: CalculatorFormat,
    v1: float = Query(1.0, gt=1.0),
    v2: float = Query(1.0, gt=1.0),
):
    """
    Calculate the division of two float values in a specified format.

    This endpoint calculates the division of two float values and returns the result in the specified format.
    Division by zero is not allowed.

    Parameters:
    - **format**: The desired format for the response. Choose from "json" or "xml".
    - **v1**: The dividend float value. (Default: 1.0)
    - **v2**: The divisor float value. (Default: 1.0)

    Responses:
    - **200 OK**: The division was calculated successfully.
        - Response JSON:
            ```
            {
                "format": str (selected format),
                "resultado": int (division of v1 by v2)
            }
            ```
    - **400 Bad Request**: Division by zero or invalid input.
        - Response JSON:
            ```
            {
                "detail": "Can't divide by 0"
            }
            ```
    - **422 Unprocessable Entity**: Validation error.
        - Response JSON:
            ```
            {
                "detail": [
                    {
                        "loc": ["query", "v1"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    },
                    {
                        "loc": ["query", "v2"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    }
                ]
            }
            ```
    """
    if v2 == 0 or v1 == 0:
        print("resultado: cannot divide with 0")
        return {"resultado": "can't divide with 0"}

    result = int(calc.divide(v1, v2))
    print(f"'resultado': {result}")
    logger.info(f"'resultado divide_format': {result}")
    return {"format": format, "resultado": result}


"""
BODY REQUEST
Body is a function that takes in an argument. 
The argument can be anything, but it's usually used 
to take in data from the body of a HTTP request. 
The Body function returns whatever was passed into 
it as its first parameter. In this case, we're passing 
in ... which means that name is required and will throw 
an error if not provided when calling create_user().
"""


@app.post("/multiply-parameters")
async def multiply(text: str = Body(...)):  # (...) means that the argument is required
    """
    Calculate the division of two float values in a `a*b` format, where a and b are int types.

    This endpoint calculates the division of two float values and returns the result in the specified format.
    Division by zero is not allowed.

    Parameters:
    - **format**: The desired format for the response. Choose from "json" or "xml".
    - **v1**: The dividend float value. (Default: 1.0)
    - **v2**: The divisor float value. (Default: 1.0)

    Responses:
    - **200 OK**: The division was calculated successfully.
        - Response JSON:
            ```
            {
                "format": str (selected format),
                "resultado": int (division of v1 by v2)
            }
            ```
    - **400 Bad Request**: Division by zero or invalid input.
        - Response JSON:
            ```
            {
                "detail": "Can't divide by 0"
            }
            ```
    - **422 Unprocessable Entity**: Validation error.
        - Response JSON:
            ```
            {
                "detail": [
                    {
                        "loc": ["query", "v1"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    },
                    {
                        "loc": ["query", "v2"],
                        "msg": "value is not a valid float",
                        "type": "type_error.float"
                    }
                ]
            }
            ```
    """
    try:
        values = text.split("*")
        v1 = int(values[0])
        v2 = int(values[1])
        print(f"v1:{v1}, v2:{v2}")
        logger.debug(f"v1:{v1}, v2:{v2}")
        print(type(v1), type(v2))
        if isinstance(v1, int) and isinstance(v2, int):
            result = int(calc.multiply(v1, v2))
            print(f"'resultado': {result}")
            logging.info(f"'resultado': {result}")
            return {"resultado": result}

    except Exception as e:
        print(f"Error: {str(e)}")
        logging.exception(f"Error: {str(e)}")
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={
                "message": "resultado: invalid multiplication string.",
                "hints": [
                    "Check the numbers",
                    "Must be 'int*int', example 1*1",
                ],
            },
        ) from e


"""
PATH PARAMETERS
Path is a class that validates the input of an endpoint. 
It's part of fastapi and it has several parameters:

ge (greater than or equal to)
gt (greater than)
lt (less than)
le (less than or equal to). 

These are used for numbers, but there are also other parameters like 
min_lenght and max_length which can be used with strings. 
There's also regex parameter which 
takes in regular expressions as arguments. This allows you to validate 
inputs based on patterns such as email addresses, phone numbers etc...
"""


@app.get("/multiply-regex/{text}")
async def multiply_regex(text: str = Path(..., regex=r"[0-9]\*[0-9]")):
    """
    Multiply two integers specified in a string format.

    This endpoint multiplies two integers specified in a string format "a*b", where a and b are integer values.

    Parameters:
    - **text**: The string containing two integers to be multiplied (format: "a*b").

    Responses:
    - **200 OK**: The multiplication was calculated successfully.
        - Response JSON:
            ```
            {
                "resultado": int (multiplication of a and b)
            }
            ```
    - **400 Bad Request**: Invalid input or multiplication string.
        - Response JSON:
            ```
            {
                "detail": {
                    "message": "resultado: invalid multiplication string.",
                    "hints": [
                        "Check the numbers",
                        "Must be 'int*int', example 1*1"
                    ]
                }
            }
            ```
    """
    values = text.split("*")
    v1 = int(values[0])
    v2 = int(values[1])

    print(type(v1), type(v2))
    logging.debug(type(v1), type(v2))
    if isinstance(v1, int) and isinstance(v2, int):
        result = int(calc.multiply(v1, v2))
        print(f"'resultado': {result}")
        logger.info(f"'resultado multiply_regex': {result}")
        return {"resultado": result}