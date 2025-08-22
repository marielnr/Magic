# Analysis of Statistics of the Baells Reservoir

This project is part of the *Programming for Data Science* course of the Degree in Applied Data Science at the UOC.
Analyze data from the Baells reservoir to identify periods of drought.
Author: Mariel Nava Rodríguez

## Project Structure

baells_analysis/
├── src/
│   ├── __init__.py
│   ├── main.py #All exercises are executed from here
│   ├── modules/
│       ├── __init__.py #to indicate that src and src/modules are packages
│       ├── data_processing.py #Here are functions to load and explore data from the df
│       ├── analysis.py #Preprocessing functions, conversions, smoothing, and a graphical demonstration of drought periods
├── tests/
│   ├── test_data_processing.py
│   ├── test_analysis.py
├── doc/ #Here the HTML documentation is generated
├── cov_html/ #Here the coverage HTML documentation is generated
├── img/ #Where the Plots of exercises 3 and 4 are saved
├── screenshots/
├── data/ #pantano_data.csv, LICENSE, .pylintrc, README.md
├── requirements.txt
                

## Facility

1. Clone or unzip the project.
3. Make sure Python 3.8 is installed
2. Install the dependencies:
```cmd
pip install -r requirements.txt

## Creating the virtual environment
1. Double-check that the terminal is in the project root directory
2. Activate the virtual environment: .\venv\Scripts\activate
3. Install the dependencies requirements.txt: pip install -r requirements.txt
4. Return to the root directory: cd ..
5.execute: pdoc -o doc src/modules/data_processing.py src/modules/analysis.py

##Before running the code
Before running the code it is important that you run in your terminal:
cd C:\Users\marie\project_pantano_baells\src
based on your route. Depending on the route you are using, the "Users\marie" will change.
Once in the src/ directory, run the script with the desired arguments:
python main.py -ex 5 # Run all exercises (1 to 5)
If you specify .py -ex 4, it will execute steps 1 through 4, and so on. The default is 5.

-ho --help: to ask for help

##For exercise 3
It is important to have pip install matplotlib in the terminal.
In my case I was running the script in Python 3.13 so I installed matplotlib there:
C:/Users/marie/AppData/Local/Programs/Python/Python313/python.exe -m pip install matplotlib
In Visual Studio sometimes plt.show() doesn't work so I put the option to save the image in the folder where the file is
Do the same in the version of Python that is running

##For exercise 4
pip install scipy

##For testing (in these tests, functions are imported from the codes to be tested with a very small csv and see possible errors)
1. Activate the virtual environment: venv\Scripts\activate
2. Make sure you have the requirements installed. If you don't have them yet, navigate to your home folder with the command: cd..
And then use the command: pip install -r requirements.txt
3. $env:PYTHONPATH = "C:\Users\marie\proyecto_pantano_baells"
pytest tests/
4. If they don't work, clearing the python cache may work:
Remove-Item -Recurse -Force src\__pycache__
Remove-Item -Recurse -Force src\modules\__pycache__
Remove-Item -Recurse -Force tests\__pycache__

##For pylint
1. Verify that pylint is installed: pip show pylint, otherwise install it: pip install pylint
2. have the virtual environment active: .\venv\Scripts\activate
3. and be in the root of the project: cd C:\Users\marie\proyecto_pantano_baells
4. to run pylint: pylint src/ tests/
5. Generate a configuration file: pylint --generate-rcfile > .pylintrc
6. Change the extension to .txt to modify it and add:
[MESSAGES CONTROL]
disable=
missing-module-docstring,
missing-function-docstring,
line-too-long,
trailing-whitespace,
missing-final-newline,
trailing-newlines,
bad-indentation,
wrong-import-position,
wrong-import-order,
import-error,
invalid-name,
possibly-used-before-assignment,
unused-variable,
unspecified-encoding,
redefined-outer-name,
reimported,
import-outside-toplevel,
unused-argument,
use-implicit-booleaness-not-comparison,
pointless-string-statement
7. Return it to the .pylintrc extension, making sure to save it as UTF-8
8. Run again in the terminal: pylint src/ tests/



