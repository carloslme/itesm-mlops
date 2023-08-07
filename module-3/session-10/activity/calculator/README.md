# Activity: Unit Tests
In this activity, you will create the unit tests to validate the functions defined in [operations.py](app/operations.py) script. Follow the instructions below to run the script. Then, create the tests.

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
Check this [file](comandos_auxiliares.md) to see more Pytest commands 