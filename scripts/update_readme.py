"""
Script Name         : update_readme.py
Script Description  : Generates and updates the README file for python-tasks repository by collecting tasks, scripts, and study notebooks information from Python files and Jupyter notebooks.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import os

# Function to generate the list content for tasks, scripts, or study notebooks
def generate_list(directory, prefix=None, is_notebook=False):
    items = []
    directory = os.path.abspath(directory)
    
    # Traverse all files or directories in the directory
    for file_name in sorted(os.listdir(directory)):
        if is_notebook:
            folder_path = os.path.join(directory, file_name)
            if os.path.isdir(folder_path) and file_name != ".ipynb_checkpoints":
                notebooks = [nb for nb in sorted(os.listdir(folder_path)) if nb.endswith(".ipynb")]
                items.append((file_name, notebooks))
        else:
            if prefix is None or (prefix and file_name.startswith(prefix) and file_name.endswith(".py")):
                file_path = os.path.join(directory, file_name)
                if prefix:
                    item_number, item_description, item_objective = get_task_info(file_path)
                    items.append((item_number, item_description, item_objective))
                else:
                    item_title, item_description = get_script_info(file_path)
                    items.append((item_title, item_description, file_name))
    return items

# Function to read the first few lines of the Python file to get task information
def get_task_info(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        task_number = lines[1].strip().split(": ")[-1]          # Extract task number
        task_description = lines[2].strip().split(": ")[-1]     # Extract task description
        task_objective   = lines[3].strip().split(": ")[-1]     # Extract task objective
        
        return task_number, task_description, task_objective

# Function to read the first two lines of the Python file to get script information
def get_script_info(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
        script_title = lines[1].strip().split(": ")[-1]         # Extract script title
        script_description = lines[2].strip().split(": ")[-1]   # Extract script description
        
        return script_title, script_description

# Function to update the .gitignore file to include .ipynb_checkpoints
def update_gitignore():
    gitignore_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".gitignore"))
    with open(gitignore_path, "a+") as gitignore:
        gitignore.seek(0)
        lines = gitignore.readlines()
        if ".ipynb_checkpoints\n" not in lines:
            gitignore.write("\n.ipynb_checkpoints\n")

# Generate the updated README.md content
def update_readme():
    # Define the path to the README file in the parent directory
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    readme_path = os.path.join(parent_directory, "README.md")
    
    with open(readme_path, "w") as readme:
        readme.write("# python-tasks\n\n")
        readme.write("#### A collection of Python programming tasks and exercises completed as part of the Embedded Linux Diploma under the supervision of [Eng. Moatasem Elsayed](https://www.linkedin.com/in/moatasem-el-sayed/)\n\n")
        readme.write("## Table of Contents\n")
        readme.write("1. [Introduction](#introduction)\n")
        readme.write("2. [Task List](#task-list)\n")
        readme.write("3. [Scripts](#scripts)\n")
        readme.write("4. [Py-Study-Notebooks](#py-study-notebooks)\n")
        readme.write("5. [Installation](#installation)\n")
        readme.write("6. [Usage](#usage)\n")
        readme.write("7. [Contributing](#contributing)\n\n")
        
        readme.write("## Introduction\n")
        readme.write("This repository contains a series of Python programming tasks and exercises that I completed as part of the Embedded Linux Diploma. Each task is designed to improve programming skills and understanding of Python.\n\n")
        
        readme.write("## Task List\n")
        readme.write("Below is a list of tasks included in this repository, along with brief descriptions:\n\n")
        
        # Generate task list
        tasks = generate_list(os.path.join(parent_directory, "tasks"), "task")
        for task_number, task_description, task_objective in tasks:
            readme.write(f"{task_number}. **[Task {task_number}: {task_description}](tasks/task{task_number}.py)**\n")
            readme.write(f"   - Objective: {task_objective}\n\n")
        
        readme.write("## Scripts\n")
        readme.write("Below is a list of scripts included in this repository, along with brief descriptions:\n\n")
        
        # Generate script list
        scripts = generate_list(os.path.join(parent_directory, "scripts"))
        for script_title, script_description, script_file in scripts:
            readme.write(f"**[Script: {script_title}](scripts/{script_file})**\n")
            readme.write(f"   - Description: {script_description}\n\n")
        
        readme.write("## Py-Study-Notebooks\n")
        readme.write("Below is a list of study notebooks included in this repository, along with brief descriptions:\n\n")
        
        # Generate py-study-notebooks list
        notebooks = generate_list(os.path.join(parent_directory, "py-study-notebooks"), is_notebook=True)
        for folder, notebook_files in notebooks:
            readme.write(f"**Study Folder: {folder}**\n")
            for notebook_file in notebook_files:
                readme.write(f"   - [Notebook: {notebook_file}](py-study-notebooks/{folder}/{notebook_file})\n")
            readme.write("\n")
        
        readme.write("## Installation\n")
        readme.write("To run the tasks and scripts, you'll need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/).\n\n")
        
        readme.write("Clone the repository to your local machine using:\n")
        readme.write("```\n")
        readme.write("git clone https://github.com/rizk-omarsherif/python-tasks.git\n")
        readme.write("```\n\n")
        
        readme.write("Navigate to the project directory:\n")
        readme.write("```\n")
        readme.write("cd python-tasks\n")
        readme.write("```\n\n")
        
        readme.write("## Usage\n")
        readme.write("Each task, script, and study notebook is contained in its own file within the `tasks`, `scripts`, and `py-study-notebooks` directories respectively. To run a task or script, execute the corresponding Python file. For example:\n")
        readme.write("```\n")
        readme.write("python tasks/task1.py\n")
        readme.write("```\n")
        readme.write("or\n")
        readme.write("```\n")
        readme.write("python scripts/script1.py\n")
        readme.write("```\n\n")
        readme.write("To open a study notebook, navigate to the appropriate folder within `py-study-notebooks` and open the Jupyter notebook file using Jupyter Notebook or JupyterLab. For example:\n")
        readme.write("```\n")
        readme.write("jupyter notebook py-study-notebooks/00_introduction-to-python/00_introduction-to-python.ipynb\n")
        readme.write("```\n\n")
        
        readme.write("## Contributing\n")
        readme.write("If you would like to contribute, please fork the repo, create a new branch, and submit a pull request. Contributions are welcome!\n\n")
        readme.write("We are all learning, so don't hesitate to submit your changes or improvements. Your contributions help make this repository better for everyone.\n")

# Main function to update README.md
if __name__ == "__main__":
    update_gitignore()
    update_readme()
