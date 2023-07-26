from sklearn.datasets import load_iris

import numpy as np

from sklearn.linear_model import LogisticRegression

# Load data from sklearn
X, y = load_iris(return_X_y=True)

# Train the model using regresion logistic
clf = LogisticRegression(solver='lbfgs',
                         max_iter=1000,
                         multi_class='multinomial').fit(X, y)
# Define iris types
iris_type = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}


# Define dummy values
sepal_length, sepal_width, petal_length, petal_width = 2, 3, 4, 6

X = [sepal_length, sepal_width, petal_length, petal_width]


# Make a prediction

prediction = clf.predict_proba([X])
print({'Class': iris_type[np.argmax(prediction)],
      'Probability': round(max(prediction[0]), 2)})
