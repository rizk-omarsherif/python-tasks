"""
Task Number      : 4
Task Description : Write a Python program which accepts the radius of a circle from the user and compute the area.
Task Objective   : This task demonstrates how to perform simple mathematical calculations.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import math

def get_area(radius):
    """
    Calculate the area of a circle given its radius.

    Args:
    - radius (float or int): The radius of the circle.

    Returns:
    - float: The calculated area of the circle.
    """
    return math.pi * radius ** 2


# Prompt the user to enter the radius of the circle
radius = float(input("Enter the radius of the circle: "))

# Print the input radius and the calculated area of a circle
# The format {:.2f} ensures the area is displayed with two decimal places.
# Using {:.2} would display two significant digits regardless of decimal point position.
print(f"Area of circle with radius {radius} is {get_area(radius):.2f}")
