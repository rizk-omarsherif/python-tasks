"""
Task Number      : 7
Task Description : Write a Python program to count the number of words in a file
Task Objective   : This task is an exercise on how to deal with files in Python

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

def file_words_count(file_name):
    with open(file_name) as f:
        return(f.read().split())

if __name__ == "__main__": 
    
    file_name = input("Enter File Name: ")
    print(f"Number of words in {file_name} is {len(file_words_count(file_name))} words")