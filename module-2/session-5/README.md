# Continuos Integration Part 1
Instructor: Carlos Mejia

## Pre-commits
Pre-commits are automated checks that run on your code before you commit changes, helping ensure code quality and consistency. In this guide, we'll use the `pre-commit` tool to set up pre-commits for Python projects in Visual Studio Code (VSC).

### Prerequisites

1. Python is installed on your system.
2. Visual Studio Code (VSC) is installed on your system.
3. `pip` is installed on your system.

### Step 1: Install `pre-commit`

First, you need to install the `pre-commit` tool on your system. Open your terminal or command prompt and run the following command:

```bash
pip install pre-commit
```


### Step 2: Create a Pre-Commit Configuration File
Create a file named `.pre-commit-config.yaml` in the root of your Python project. This file will define the pre-commit hooks to be executed.

### Step 3: Configure Pre-Commit Hooks
In the `.pre-commit-config.yaml` file, define the pre-commit hooks you want to run. Each hook represents a specific check on your code. There are many pre-configured hooks available, and you can also create custom hooks if needed.

Here's the code `.pre-commit-config.yaml` with the pre-commit hooks we will use in this course for Python:

```yaml
repos:
  - repo: https://github.com/pre-commit/mirrors-autopep8
    rev: ''  # Specify a specific version/tag/commit or leave empty for the latest version
    hooks:
      - id: autopep8
        exclude: '^$'  # Specify files or patterns to exclude, '^$' excludes nothing (all files will be checked)

- repo: https://github.com/PyCQA/flake8
  rev: 6.0.0
  hooks:
  - id: flake8
    args: [--ignore=E501]
```

### Step 4: Initialize Pre-Commit for Your Project
After creating the `.pre-commit-config.yaml` file, initialize pre-commit for your project. Open your terminal or command prompt, navigate to the root directory of your project, and run the following command:
```bash
pre-commit install
```
Output
```bash
pre-commit installed at .git/hooks/pre-commit
```
> **NOTE**  
If you want to see the default hidden folder `.git`, follow the steps in this link: https://linuxpip.org/vscode-show-hidden-files/

### Step 5: Commit Your Changes
With the pre-commit hooks installed, you can now make changes to your Python code. When you're ready to commit your changes, run the following command to trigger the pre-commit checks:

```bash
git commit -m "add pre-commit file"
```
Output

 <details open>
    <summary>Pre-commit output, click to collapse</summary>
    ```bash
    [WARNING] The 'rev' field of repo 'https://github.com/pre-commit/mirrors-autopep8' appears to be a mutable reference (moving tag / branch).  Mutable references are never updated after first install and are not supported.  See https://pre-commit.com/#using-the-latest-version-for-a-repository for more details.  Hint: `pre-commit autoupdate` often fixes this.
    [INFO] Initializing environment for https://github.com/pre-commit/mirrors-autopep8.
    [INFO] Initializing environment for https://github.com/PyCQA/flake8.
    [INFO] Installing environment for https://github.com/pre-commit/mirrors-autopep8.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    [INFO] Installing environment for https://github.com/PyCQA/flake8.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    autopep8.............................................(no files to check)Skipped
    flake8...............................................(no files to check)Skipped
    [main 210cf52] add pre-commit file
    3 files changed, 77 insertions(+)
    create mode 100644 .pre-commit-config.yaml
    create mode 100644 module-2/session-5/README.md
    ```
    </details>
    

Pre-commit will run all the defined hooks on the files you've staged for the commit. If any issues are found (e.g., trailing whitespace, linting errors, etc.), the commit will be halted, and you'll need to address the problems before you can successfully commit.

### Step 6. Add a new file
* Please create a python file called `iris.py`, and copy the following code into it.
```python
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
print({'class': iris_type[np.argmax(prediction)],'probability': round(max(prediction[0]), 2)})
```
* Try to commit the file with the following message running in the console:
```bash
git commit -m "add iris file"
```
Output:
```bash
[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to /Users/.../.cache/pre-commit/patch1690330398-66588.
[WARNING] The 'rev' field of repo 'https://github.com/pre-commit/mirrors-autopep8' appears to be a mutable reference (moving tag / branch).  Mutable references are never updated after first install and are not supported.  See https://pre-commit.com/#using-the-latest-version-for-a-repository for more details.  Hint: `pre-commit autoupdate` often fixes this.
autopep8.................................................................Failed
- hook id: autopep8
- files were modified by this hook
flake8...................................................................Passed
[WARNING] Stashed changes conflicted with hook auto-fixes... Rolling back fixes...
[INFO] Restored changes from /Users/.../.cache/pre-commit/patch1690330398-66588.
```
This means that `flake8` worked, and `autopep8` did not.

### Step 7. Running `autopep8`
To fix the `autopep8`, follow the instructions below:
1. Install it using `pip`:
    ```bash
    pip install autopep8
    ```
2. Run `autopep8` with the Python file
    ```bash
    autopep8 --in-place --aggressive --aggressive module-2/session-5/iris.py
    ```
    The above command will apply more aggressive formatting to your Python file.
3. Run again the commit command, and you will see that the test has passed.
    ```bash
    git commit -m "add iris file"
    ```
    Output:
    ```
    `git add .pre-commit-config.yaml` to fix this.
    (pre-commits-env) (base) carloslme:itesm-mlops carlos$ git commit -m "add iris file"
    [WARNING] Unstaged files detected.
    [INFO] Stashing unstaged files to /Users/carlos/.cache/pre-commit/patch1690331306-67140.
    [INFO] Initializing environment for https://github.com/pre-commit/mirrors-autopep8.
    [INFO] Installing environment for https://github.com/pre-commit/mirrors-autopep8.
    [INFO] Once installed this environment will be reused.
    [INFO] This may take a few minutes...
    autopep8.................................................................Passed
    flake8...................................................................Passed
    [INFO] Restored changes from /Users/carlos/.cache/pre-commit/patch1690331306-67140.
    [main 8373807] add iris file
    2 files changed, 33 insertions(+), 1 deletion(-)
    create mode 100644 module-2/session-5/iris.py
    ```

### Step 8. Modify the `.pre-commit-config.yaml` file
* Include this code to add an explanation about what is wrong in the code.

    > **NOTE**  
        Do not forget to change again the `iris.py` file to the original code in previous steps.

* Run the commit message again, and you should see something like this:
    ```bash
    ...
    [INFO] Stashing unstaged files to /Users/carlos/.cache/pre-commit/patch1690331670-67562.
    autopep8.................................................................Passed
    flake8...................................................................Failed
    - hook id: flake8
    - exit code: 1

    module-2/session-5/iris.py:23:1: E303 too many blank lines (3)
    module-2/session-5/iris.py:30:1: E303 too many blank lines (3)
    module-2/session-5/iris.py:33:49: E231 missing whitespace after ','
    module-2/session-5/iris.py:33:95: W292 no newline at end of file
    ```
* Run again the `autopep8` and the file will be modified to handle the errors.