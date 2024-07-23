import os

# Function to generate the Task List section content
def generate_task_list():
    task_list = []
    # Traverse all files in the current directory
    for file_name in sorted(os.listdir()):
        if file_name.startswith("task") and file_name.endswith(".py"):
            task_number, task_description, task_objective = get_task_info(file_name)        # Get task number and description from file
            task_list.append((task_number, task_description, task_objective))
    return task_list

# Function to read the first two lines of the Python file to get task number and description
def get_task_info(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        task_number = lines[1].strip().split(": ")[-1]          # Extract task number
        task_description = lines[2].strip().split(": ")[-1]     # Extract task description
        task_objective   = lines[3].strip().split(": ")[-1]     # Extract task objective
        
        return task_number, task_description, task_objective

# Generate the updated README.md content
def update_readme():
    with open("README.md", "w") as readme:
        readme.write("# python-tasks\n\n")
        readme.write("#### A collection of Python programming tasks and exercises completed as part of the Embedded Linux Diploma under the supervision of [Eng. Moatasem Elsayed](https://www.linkedin.com/in/moatasem-el-sayed/)\n\n")
        readme.write("## Table of Contents\n")
        readme.write("1. [Introduction](#introduction)\n")
        readme.write("2. [Task List](#task-list)\n")
        readme.write("3. [Installation](#installation)\n")
        readme.write("4. [Usage](#usage)\n")
        readme.write("5. [Contributing](#contributing)\n\n")
        
        readme.write("## Introduction\n")
        readme.write("This repository contains a series of Python programming tasks and exercises that I completed as part of the Embedded Linux Diploma. Each task is designed to improve programming skills and understanding of Python.\n\n")
        
        readme.write("## Task List\n")
        readme.write("Below is a list of tasks included in this repository, along with brief descriptions:\n\n")
        
        # Generate task list
        tasks = generate_task_list()
        for task_number, task_description, task_objective in tasks:
            readme.write(f"{task_number}. **[Task {task_number}: {task_description}](task{task_number}.py)**\n")
            readme.write(f"   - Objective: {task_objective}\n\n")  # Add objective
        
        readme.write("## Installation\n")
        readme.write("To run the tasks, you'll need to have Python installed on your machine. You can download it from [python.org](https://www.python.org/).\n\n")
        
        readme.write("Clone the repository to your local machine using:\n")
        readme.write("```\n")
        readme.write("git clone https://github.com/rizk-omarsherif/python-tasks.git\n")
        readme.write("```\n\n")
        
        readme.write("Navigate to the project directory:\n")
        readme.write("```\n")
        readme.write("cd python-tasks\n")
        readme.write("```\n\n")
        
        readme.write("## Usage\n")
        readme.write("Each task is contained in its own file. To run a task, execute the corresponding Python file. For example:\n")
        readme.write("```\n")
        readme.write("python task1.py\n")
        readme.write("```\n\n")
        
        readme.write("## Contributing\n")
        readme.write("If you would like to contribute, please fork the repo, create a new branch, and submit a pull request. Contributions are welcome!\n\n")
        readme.write("We are all learning, so don't hesitate to submit your changes or improvements. Your contributions help make this repository better for everyone.\n")

# Main function to update README.md
if __name__ == "__main__":
    update_readme()
