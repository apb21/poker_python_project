# Poker Python Project

A project to practice data analysis techniques on the game of poker.

## Software Requirements

+ Git
    - Used to clone this project from GitHub, and to version control changes made.
    - Install from https://git-scm.com/install
+ UV
    - Used to manage the python environment, install version of python and install python packages.
    - Install from https://docs.astral.sh/uv/getting-started/installation/

## Getting started with development

Switch to the development branch to get the in-progress work.

> git branch develop

Run the following command to install the development environment for the package.

> uv pip install -e .[dev]

This will install the module "in-place" as well as the development-only dependencies.

Run main.py to get an example of functionality available so far.

> uv run main.py

Run the following command to run all exisiting tests against the project (they should all pass).

> uv run python -m pytest

Files defining tests can be found in the /tests directory.

## Visual Studio Code

The project is written with and designed to be developed in Visual Studio Code (including "Code - OSS").

### Visual Studio Code Recommended Settings

The project comes with an example set of settings that you may wish to activate.

Rename ./.vscode/settings.smaple.json to ./.vscode/settings.json to activate the settings.

These mostly relate to telling VS Code to use the uv tool when running different scripts.

### Visual Studio Code Extensions

The following official (from Microsoft) VS Code extensions are recommended when developing this project.

+ Python
+ Black Formatter
+ Flake8
+ isort
+ Pylint
+ MyPy Type Checker

