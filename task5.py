"""
Task Number      : 5
Task Description : Write a Python program to print the calendar of a given month and year.
Task Objective   : This task demonstrates how to use Python's calendar module.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import calendar

# Prompt the user to enter the year
year  = int(input("Enter Year: "))

# Prompt the user to enter the month
month = int(input("Enter Month: "))

# Print the calendar of a given month and year
print(f"\n{calendar.month(year,month)}")