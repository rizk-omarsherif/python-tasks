# python-tasks

#### A collection of Python programming tasks and exercises completed as part of the Embedded Linux Diploma under the supervision of [Eng. Moatasem Elsayed](https://www.linkedin.com/in/moatasem-el-sayed/)

## Table of Contents
1. [Introduction](#introduction)
2. [Task List](#task-list)
3. [Scripts](#scripts)
4. [Py-Study-Notebooks](#py-study-notebooks)
5. [Installation](#installation)
6. [Usage](#usage)
7. [Contributing](#contributing)

## Introduction
This repository contains a series of Python programming tasks and exercises that I completed as part of the Embedded Linux Diploma. Each task is designed to improve programming skills and understanding of Python.

## Task List
Below is a list of tasks included in this repository, along with brief descriptions:

1. **[Task 1: Write a Python program to count the number 4 in a given list.](tasks/task1.py)**
   - Objective: This task focuses on list iteration and basic counting operations.

2. **[Task 2: Write a Python program to test whether a passed letter is a vowel or not.](tasks/task2.py)**
   - Objective: This task is useful for practicing conditional statements and understanding string operations.

3. **[Task 3: Write a Python program to access environment variables.](tasks/task3.py)**
   - Objective: This task demonstrates how to interact with the system environment using Python's `os` module.

4. **[Task 4: Write a Python program which accepts the radius of a circle from the user and compute the area.](tasks/task4.py)**
   - Objective: This task demonstrates how to perform simple mathematical calculations.

5. **[Task 5: Write a Python program to print the calendar of a given month and year.](tasks/task5.py)**
   - Objective: This task demonstrates how to use Python's calendar module.

6. **[Task 6: Write a Python program to count the number of lines in a text file](tasks/task6.py)**
   - Objective: This task is an exercise on how to deal with files in Python.

7. **[Task 7: Write a Python program to count the number of words in a file](tasks/task7.py)**
   - Objective: This task is an exercise on how to deal with files in Python

8. **[Task 8: Write a Python script to fetch Bitcoin rates from an API and save the data to a CSV file.](tasks/task8.py)**
   - Objective: This task is an exercise in using the `requests` module to interact with web APIs and `pandas` to handle and store data in a tabular format.

9. **[Task 9: Use PyAutoGUI to install VS Code C++ extensions](tasks/task9.py)**
   - Objective: This task is an exercise in using `PyAutoGUI` to automate simple tasks

## Scripts
Below is a list of scripts included in this repository, along with brief descriptions:

**[Script: generate_header_files.py](scripts/generate_header_files.py)**
   - Description: Creates new task files with a predefined header, prompting the user for task details to ensure consistency across the repository.

**[Script: install-vs-extensions.py](scripts/install-vs-extensions.py)**
   - Description: Automates the installation of VS Code extensions using PyAutoGUI, with an added PySide6 GUI for enhanced user-friendliness.

**[Script: update_readme.py](scripts/update_readme.py)**
   - Description: Generates and updates the README file for python-tasks repository by collecting tasks, scripts, and study notebooks information from Python files and Jupyter notebooks.

## Py-Study-Notebooks
Below is a list of study notebooks included in this repository, along with brief descriptions:

**Study Folder: 00_introduction-to-python**
   - [Notebook: 00_introduction-to-python.ipynb](py-study-notebooks/00_introduction-to-python/00_introduction-to-python.ipynb)

**Study Folder: 01_data-types**
   - [Notebook: 00_intro-to-python-data-types.ipynb](py-study-notebooks/01_data-types/00_intro-to-python-data-types.ipynb)
   - [Notebook: 01_numeric-types.ipynb](py-study-notebooks/01_data-types/01_numeric-types.ipynb)
   - [Notebook: 02_strings.ipynb](py-study-notebooks/01_data-types/02_strings.ipynb)
   - [Notebook: 03_lists.ipynb](py-study-notebooks/01_data-types/03_lists.ipynb)
   - [Notebook: 04_tuples.ipynb](py-study-notebooks/01_data-types/04_tuples.ipynb)
   - [Notebook: 05_dictionaries.ipynb](py-study-notebooks/01_data-types/05_dictionaries.ipynb)
   - [Notebook: 06_sets.ipynb](py-study-notebooks/01_data-types/06_sets.ipynb)
   - [Notebook: 07_containers-comparison.ipynb](py-study-notebooks/01_data-types/07_containers-comparison.ipynb)

**Study Folder: 02_operators**
   - [Notebook: 01_arithmetic-operators.ipynb](py-study-notebooks/02_operators/01_arithmetic-operators.ipynb)
   - [Notebook: 02_bitwise-operators.ipynb](py-study-notebooks/02_operators/02_bitwise-operators.ipynb)
   - [Notebook: 03_assignment-operators.ipynb](py-study-notebooks/02_operators/03_assignment-operators.ipynb)
   - [Notebook: 04_relational-operators.ipynb](py-study-notebooks/02_operators/04_relational-operators.ipynb)
   - [Notebook: 05_logical-operators.ipynb](py-study-notebooks/02_operators/05_logical-operators.ipynb)
   - [Notebook: 06_membership-and-identity-operators.ipynb](py-study-notebooks/02_operators/06_membership-and-identity-operators.ipynb)

**Study Folder: 03_control-flow**
   - [Notebook: 01_conditional-statement.ipynb](py-study-notebooks/03_control-flow/01_conditional-statement.ipynb)
   - [Notebook: 02_loops.ipynb](py-study-notebooks/03_control-flow/02_loops.ipynb)

**Study Folder: 04_functions**
   - [Notebook: 01_functions.ipynb](py-study-notebooks/04_functions/01_functions.ipynb)

**Study Folder: 05_oop-in-python**
   - [Notebook: 01_Introduction-to-oop.ipynb](py-study-notebooks/05_oop-in-python/01_Introduction-to-oop.ipynb)
   - [Notebook: 02_encapsulation-inheritance.ipynb](py-study-notebooks/05_oop-in-python/02_encapsulation-inheritance.ipynb)
   - [Notebook: 03_advanced-oop-concepts.ipynb](py-study-notebooks/05_oop-in-python/03_advanced-oop-concepts.ipynb)

**Study Folder: 06_threading**
   - [Notebook: Untitled.ipynb](py-study-notebooks/06_threading/Untitled.ipynb)

**Study Folder: 07_sockets**

**Study Folder: 08_gui-tkinter**

## Installation
To run the tasks and scripts, you'll need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

Clone the repository to your local machine using:
```
git clone https://github.com/rizk-omarsherif/python-tasks.git
```

Navigate to the project directory:
```
cd python-tasks
```

## Usage
Each task, script, and study notebook is contained in its own file within the `tasks`, `scripts`, and `py-study-notebooks` directories respectively. To run a task or script, execute the corresponding Python file. For example:
```
python tasks/task1.py
```
or
```
python scripts/script1.py
```

To open a study notebook, navigate to the appropriate folder within `py-study-notebooks` and open the Jupyter notebook file using Jupyter Notebook or JupyterLab. For example:
```
jupyter notebook py-study-notebooks/00_introduction-to-python/00_introduction-to-python.ipynb
```

## Contributing
If you would like to contribute, please fork the repo, create a new branch, and submit a pull request. Contributions are welcome!

We are all learning, so don't hesitate to submit your changes or improvements. Your contributions help make this repository better for everyone.
