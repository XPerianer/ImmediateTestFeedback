# ImmediateTestFeedback

This repo serves as the starting point for installing and
tweaking the `ImmediateTestFeedback` Prototype build inside
the PLCTE seminar at the software architecture chair of the Hasso-Plattner-Institute.

# Introduction
Changing software without correctly understanding it often leads to confusion, as developers do not understand how the change corresponds to the new observed behaviour of the system.
Today, many software systems are equipped with a test suite.
Test suites document code and give feedback on changed program behaviour.
We explored ways to use test suites for software comprehension. We implemented a tool that provides additional visualization and gives immediate feedback on software changes.
Information about changes in the software and their implications to the test suite are collected using mutation testing. The tool uses this information to present relevant test cases for developers, and additionally prioritize test executions for immediate feedback.

This system uses mutation testing data to present relevant test cases for developers and additionally prioritize test executions for immediate feedback.

# How does it work?
Architectural Overview:
![architecture(1)](https://user-images.githubusercontent.com/5360508/109017640-a7b9da80-76b7-11eb-9c74-7dbc74ae4cc9.png)

The system consists of serveral parts:
## Mutation Testing Dataset
The dataset needed for analysis can be generated for a python repository tested with `pytest` by using the tool [Mutester](https://github.com/XPerianer/Mutester).
This will generate a basic pandas dataframe containing the mutation testing data.
Further preprocessing is now needed to bring it into a form that is useable for the `Backend`.



# Installation
1.  Clone the repository you want to get immediate test feedback during development.
    Examplatory, we will use flask
    ```
    git clone https://github.com/pallets/flask.git
    ```
1.  Generate a pandas dataframe containing mutation Testing Data (see [Mutester](https://github.com/XPerianer/Mutester))
    This will generate a pandas dataframe (in this example, `flask.pkl`)
1. Clone this repository including all submodules.
    ```
    git clone --recurse-submodules https://github.com/XPerianer/ImmediateTestFeedback
    ```
1. Install the dependencies for the [Jupyter Notebook](preprocessing.ipynb). Usually, you want to create a virtual environment:
    ```
    python -m venv venv
    pip install -r reqirements.txt
    ```
1. Start the jupyter notebook:
    ```
    jupyter notebook preprocess.ipynb
    ```
    and follow the steps in the [Jupyter Notebook](preprocessing.ipynb) to
    generate a `.joblib` file that can be loaded by the backend.
1.  Install the Backend:
    ```
    cd TestingBackend
    python -m venv venv
    . venv/bin/activate
    pip install -e . -r requirements.txt
    ```
1.  Set up the Backend:
    In `config.cfg`, the pathes need to be correclty set:
    * `PREDICTOR_MODEL_JOBLIB_FILE` path to the `.joblib` file generated
    * `MUTATION_TESTING_FILE` should be the path to the mutation dataset, `flask.pkl`
    * `REPOSITORY_PATH` should be the path to the repository you want to develop

1.  Visual Studio Code is now ready to load.
