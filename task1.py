
"""
Task Number: 1
Task Description: Write a Python program to count the number 4 in a given list.

Author: Omar Rizk
Course: Python Programming
Diploma: Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

def is_numeric(x):
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

print("The list you entered is:", int_list)

print(int_list.count(4))