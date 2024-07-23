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
    
    file_name = f"task{task_number}.py"
    with open(file_name, "w") as file:
        file.write(header)

    print(f"{file_name} has been created with the header.")

if __name__ == "__main__":
    main()