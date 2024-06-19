
"""
Task Number: 3
Task Description: Write a Python program to access environment variables.

Author: Omar Rizk
Course: Python Programming
Diploma: Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import os

# Access a specific environment variable
def access_env_variable(var_name):
    """
    Retrieve the value of a specific environment variable.

    Args:
    - var_name (str): The name of the environment variable.

    Returns:
    - str: The value of the environment variable if it exists, or None if not found.
    """
    return os.getenv(var_name)

#Accessing the HOME environment variable
home_dir = access_env_variable('HOME')
if home_dir:
    print(f"The value of HOME environment variable is: {home_dir}")
else:
    print("HOME environment variable is not set.")
