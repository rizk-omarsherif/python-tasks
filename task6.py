"""
Task Number      : 6
Task Description : Write a Python program to count the number of lines in a text file
Task Objective   : This task is an exercise on how to deal with files in Python.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

def file_lines_length(file_name):
    with open(file_name) as f:
        for i, l in enumerate(f):
            pass
    return i+1

if __name__ == "__main__": 
    
    file_name = input("Enter File Name: ")
    print(f"NUmber of lines in {file_name} = {file_lines_length(file_name)}")