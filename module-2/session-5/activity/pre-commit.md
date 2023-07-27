# Activity Session 5: pre-commit

In this activity, you will modify the [`.pre-commit-config.yaml`](./.pre-commit-config.yaml) file to meet the following requirements once you do commit.

Follow the instructions in the [README.md](../README.md) if you do not know how to setup the pre-commits.

## Repos
1. **Sort libraries**  
Include a repo that sort the imports of dependencies expressed in the [PEP8 style for Imports](https://pep8.org/#imports).
    
    For example, having this code and before sorting:
    ```python
    from my_lib import Object

    import os

    from my_lib import Object3

    from my_lib import Object2

    import sys

    from third_party import lib15, lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8, lib9, lib10, lib11, lib12, lib13, lib14

    import sys

    from __future__ import absolute_import

    from third_party import lib3

    print("Hey")
    print("yo")
    ```

    After sorting:
    ```python
    from __future__ import absolute_import

    import os
    import sys

    from third_party import (lib1, lib2, lib3, lib4, lib5, lib6, lib7, lib8,
                            lib9, lib10, lib11, lib12, lib13, lib14, lib15)

    from my_lib import Object, Object2, Object3

    print("Hey")
    print("yo")
    ```

    > HINT  
    The `isort` Python library can help you with this, but **you have to install it in the pre-commit** file.

2. **Delete unused imports**  
    Include another repo to remove the unused imports every commit.  

    For example, if you are including the `import sys` Python library but not using it, once you run the precommit, you should upload only the used imports.
    
    > **HINT**  
    [Autoflake](https://pypi.org/project/autoflake/) or [Pylint](https://pypi.org/project/pylint/) are a couple of alternatives to do this. Figure out how to use it in the pre-commit or **even combine them**.

## Code
The following Python code will be used to test the repos in that you have included in the `.pre-commit-config.yaml` file.

* Modify the Python `iris.py` file with this code:
    ```python
    import os # This is an unused import
    import json # This is an unused import
    from sklearn.datasets import load_iris # Import in incorrect order

    import numpy as np # Import in incorrect order
    import json # This is an unused import

    from my_library import test # This is an unused import
    from sklearn.linear_model import LogisticRegression # Import in incorrect order

    # Load data from sklearn
    X, y = load_iris(return_X_y=True)

    # Train the model using regresion logistic
    clf = LogisticRegression(solver='lbfgs',max_iter=1000,multi_class='multinomial').fit(X, y)
    # Define iris types
    iris_type = {0: 'setosa',1: 'versicolor',2: 'virginica'}


    # Define dummy values
    sepal_length, sepal_width, petal_length, petal_width = 2, 3, 4, 6

    X = [sepal_length, sepal_width, petal_length, petal_width]


    # Make a prediction

    prediction = clf.predict_proba([X])
    print({'class': iris_type[np.argmax(prediction)],'probability':round(max(prediction[0]), 2)})
    ```
* Do the commit to activate the pre-commit. The `iris.py` file output should look like this:
    ```python
    import numpy as np
    from sklearn.datasets import load_iris
    from sklearn.linear_model import LogisticRegression

    # Load data from sklearn
    X, y = load_iris(return_X_y=True)

    # Train the model using regresion logistic
    clf = LogisticRegression(
        solver='lbfgs',
        max_iter=1000,
        multi_class='multinomial').fit(X, y)
    # Define iris types
    iris_type = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}


    # Define dummy values
    sepal_length, sepal_width, petal_length, petal_width = 2, 3, 4, 6

    X = [sepal_length, sepal_width, petal_length, petal_width]


    # Make a prediction

    prediction = clf.predict_proba([X])
    print({'class': iris_type[np.argmax(prediction)],
        'probability': round(max(prediction[0]), 2)})
    ```

    The corrected code above should be the one that is going to be sent to the repository.

## Deliverable
The deliverable is the `.pre-commit-config.yaml` file with the new repos included. This has to be uploaded to your repository.

The link to share the repo link is available in the Google form provided by the instructor (TBA)