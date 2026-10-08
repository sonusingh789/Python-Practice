Python Setup and Development Environment
Python Installation

Python is the primary language for AI/ML development. Download the latest stable version (3.x) from python.org.

During installation on Windows, make sure to check "Add Python to PATH" to enable command-line access.

Verify the installation using:

python --version

or:

python3 --version

IDEs
VS Code

VS Code is a lightweight and highly extensible editor with Python extension support.

Features:

Python extension support
Integrated terminal
Debugging tools
Lightweight and customizable
Popular for general development
PyCharm

PyCharm is a full-featured IDE specifically designed for Python development.

Features:

Strong code completion
Refactoring tools
Project management
Python-specific development features
Available in Community (free) and Professional editions
Jupyter Notebook / JupyterLab

Jupyter Notebook/Lab is a browser-based interactive environment ideal for data science and machine learning.

It allows you to combine:

Python code
Output
Visualizations
Markdown notes

Install Jupyter Notebook:

pip install notebook

Or install JupyterLab:

pip install jupyterlab

Terminal / Command Line Basics

Essential commands for navigating and managing files:

Command Description
pwd Print the current working directory
cd <folder> Change directory
ls List files (Mac/Linux)
dir List files (Windows)
mkdir <name> Create a new folder
python filename.py Run a Python script
Examples

Change to a folder:

cd myproject

Create a new folder:

mkdir myproject

Run a Python script:

python app.py

Python Interpreter & REPL

The REPL (Read-Eval-Print Loop) allows you to run Python code line-by-line interactively.

Start the Python interpreter by typing:

python

or:

python3

The REPL is useful for:

Quick testing
Debugging
Experimentation
Learning Python syntax

Example:

> > > print("Hello, World!")
> > > Hello, World!

> > > 10 + 20
> > > 30

To exit the REPL, use:

exit()

Or press:

Ctrl + D

Windows: Ctrl + Z followed by Enter can also be used to exit the Python REPL.
Virtual Environments (venv)

Virtual environments allow you to isolate project dependencies, preventing package and version conflicts between different projects.

It is recommended to use a virtual environment for ML projects to manage package versions cleanly.

Create a Virtual Environment
python -m venv myenv

This creates a virtual environment named myenv.

Activate on Windows
myenv\Scripts\activate

Activate on Mac/Linux
source myenv/bin/activate

After activation, your terminal will usually show the environment name:

(myenv) C:\Projects\myproject>

Deactivate the Environment

To deactivate the virtual environment:

deactivate

Recommended Workflow for ML Projects

A typical workflow is:

# Create a project folder

mkdir my_ml_project

# Enter the project folder

cd my_ml_project

# Create a virtual environment

python -m venv myenv

# Activate on Windows

myenv\Scripts\activate

# Activate on Mac/Linux

source myenv/bin/activate

# Install required packages

pip install numpy pandas matplotlib scikit-learn

# Run your Python program

python main.py

# Deactivate when finished

deactivate
