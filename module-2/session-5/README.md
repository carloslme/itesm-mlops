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

Pre-commit will run all the defined hooks on the files you've staged for the commit. If any issues are found (e.g., trailing whitespace, linting errors, etc.), the commit will be halted, and you'll need to address the problems before you can successfully commit.