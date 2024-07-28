"""
Script Name         : generate_header_files.py
Script Description  : Creates new task files with a predefined header, prompting the user for task details to ensure consistency across the repository.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import os

def create_header(task_number, task_description, task_objective, author, course, diploma):
    header = f"""\"\"\"
Task Number      : {task_number}
Task Description : {task_description}
Task Objective   : {task_objective}

Author  : {author}
Course  : {course}
Diploma : {diploma}
\"\"\"
"""
    return header

def main():
    task_number      = input("Enter task number: ")
    task_description = input("Enter task description: ")
    task_objective   = input("Enter task objective: ")
    author = "Omar Rizk"
    course = "Python Programming"
    diploma = "Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)"

    header = create_header(task_number, task_description, task_objective, author, course, diploma)
    
    # Specify the directory path
    directory_path = os.path.join("..", "tasks")
    
    # Create the directory if it doesn't exist
    os.makedirs(directory_path, exist_ok=True)
    
    file_name = f"task{task_number}.py"
    file_path = os.path.join(directory_path, file_name)
    
    with open(file_path, "w") as file:
        file.write(header)

    print(f"{file_name} has been created in the 'tasks' directory with the header.")

if __name__ == "__main__":
    main()
