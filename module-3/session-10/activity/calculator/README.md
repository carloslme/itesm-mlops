# Activity: Unit and Integration Tests
In this activity, you will create the unit tests to validate the functions defined in [operations.py](app/operations.py) script. Follow the instructions below to run the script. Then, create the tests.

## Deliverables
**Unit tests:**
Tests for addition, subtraction, multiplication, division and the one that converts fractions to numbers.

**Integration testing:**
Carry out the test for the following mathematical operation:
(num1 + num2) * (num3 - num4)

with the following numbers
(5+5)*(1.25-0.75) = (10)*(0.5) = 5
(8+7/5)*(15-3/8) = (9.4)*(14.625) = 137.475

## Preconditions
It is assumed that you already have Python 3+ installed in its system. If not, please install it.

Check this link according to your operating system:
[Python 3 Installation & Setup Guide](https://realpython.com/installing-python/)

## Virtual Environment Installation
Open a terminal, go to the project root folder, and install `venv` with the following command.

```bash
pip3 install virtualenv
```

Then, run the following commands to create the virtual environment.
```bash
python3 -m venv ./venv
```

Activate the virtual environment.
```bash
source env/bin/activate
```

**Note**  
Disable the virtual environment using this command at the end of its example.
```bash
deactivate
```

## Library Installation
To install the necessary libraries, use this command:
```
pip3 install -r requirements.txt
```

Ready, the configuration is ready for the check the script!

## Running the code
Change the directory and run the following command
```bash
cd session-10/pytest/calculator/app/
```
Then run
```bash
python example.py
```
I should see the following data output
```bash
1.5
0.5
2.0
0.5
```


## Execute unit
Write here your commands to run the Pytest tests.

> **Note**  
Check this [auxiliar_commands](auxiliar_commands.md) to see more Pytest commands 