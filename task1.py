"""
Task Number      : 1
Task Description : Write a Python program to count the number 4 in a given list.
Task Objective   : This task focuses on list iteration and basic counting operations.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

def is_numeric(x):
    """
    Checks if an input can be converted to an integer.

    Args:
    - x: The input value to check.

    Returns:
    - True if x can be converted to an integer.
    - False otherwise.
    """
    try:
        int(x)
        return True
    except ValueError:
        return False


# Prompt the user to enter a list of items separated by spaces
user_input = input("Enter a list of items separated by spaces: ")

# Split the input string by spaces to get a list of items
str_list  = user_input.split()

# Filter out non-numeric values and convert the rest to integers
int_list = [int(item) for item in str_list if is_numeric(item)]

# Print the integer-only list
print(f"The integer-only list is: {int_list}")

# Print the count of number 4 in the integer-only list
print(f" Number 4 appears in the list {int_list.count(4)} times!")