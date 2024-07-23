"""
Task Number      : 2
Task Description : Write a Python program to test whether a passed letter is a vowel or not.
Task Objective   : This task is useful for practicing conditional statements and understanding string operations.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

def is_vowel(letter):
    """
    Check if a given letter is a vowel.

    Args:
    - letter (str): The letter to check. It should be a single character string.

    Returns:
    - True if letter is a vowel.
    - False otherwise.
    """
    # Define a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # Convert the letter to lowercase (to handle uppercase as well)
    letter = letter.lower()

    # Check if the letter is in the set of vowels
    if letter in vowels:
        return True
    else:
        return False

# Prompt the user to enter a letter
letter = input("Enter a letter: ")

# Check if the entered letter is a vowel
if is_vowel(letter):
    print(f"The letter '{letter}' is a vowel.")
else:
    print(f"The letter '{letter}' is not a vowel.")

