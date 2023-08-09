from pydantic import BaseModel


class Iris(BaseModel):
    sepal_length: float
    sepal_width: float
    # TODO: Add two missing attributes here