"""
Task Number      : 9
Task Description : Use PyAutoGUI to install VS Code C++ extensions
Task Objective   : This task is an exercise in using `PyAutoGUI` to automate simple tasks

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import pyautogui
import subprocess
from time import sleep
import os

def open_vscode():
    """
    Function to open Visual Studio Code using the 'code' command.
    """
    try:
        # Run the command that opens VS Code
        subprocess.run(["code"], check=True)
        print("VS Code opened successfully.")
    except FileNotFoundError:
        print("VS Code command 'code' not found. Make sure VS Code is installed and added to your PATH.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to open VS Code. Error: {e}")

def locate_and_click(image_paths, confidence=0.85, offset=(0, 0), sleep_time=1, retries=3):
    """
    Function to locate an image on the screen and click on it.

    Args:
        image_paths (list)             : List of paths to the images to locate on the screen.
        confidence  (float , optional) : Confidence level for image recognition.              ->  Defaults to 0.85.
        offset      (tuple , optional) : Tuple (x, y) for adjusting the click position.       ->  Defaults to (0, 0).
        sleep_time  (int   , optional) : Time to sleep after clicking.                        ->  Defaults to 1.
        retries     (int   , optional) : Number of times to retry locating the image.         ->  Defaults to 3.

    Returns:
        None
    """
    
    for image_path in image_paths:
        # Extract the image name from the path for print statements
        image_name = os.path.basename(image_path)  
        
        location = None  # Initialize the location to None
        attempt = 0      # Initialize the attempt counter
        
        while location is None and attempt < retries:
            try:
                # Attempt to locate the image on the screen with the specified confidence
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                
                if location:
                    # If the image is found, print its location and prepare to click
                    print(f"\nFound '{image_name}' at location = {location}\nClicking now...")
                else:
                    # If the image is not found, print a retry message and sleep for a while before retrying
                    print(f"\n'{image_name}' not found. Retry {attempt + 1}/{retries}")
                    sleep(1)
                    
            except pyautogui.ImageNotFoundException:
                # Handle the case where the image is not found due to an exception
                print(f"\nImageNotFoundException: '{image_name}' not found. Retry {attempt + 1}/{retries}")
                sleep(1)
                
            attempt += 1  # Increment the attempt counter
            
        if location:
            # If the location is found, click on the image with the specified offset
            pyautogui.click(location.left + offset[0], location.top + offset[1])
            sleep(sleep_time)  # Sleep for the specified time after clicking
            return location  # Return the location where the image was found and clicked
    
    # If none of the images are found after all retries, print a failure message
    print(f"\nCould not locate any of the images {image_paths} on screen after {retries} attempts each.")
    return None

def install_extension(extension_name, search_offset=(100, 20), install_offset=(20, 20), clear_offset=(20, 10)):
    """
    Function to search and install a VS Code extension.

    Args:
        extension_name (str)        : Name of the extension to install.
        search_offset  (tuple)      : Offset for the search bar click. Defaults to (100, 20).
        install_offset (tuple)      : Offset for the install button click. Defaults to (20, 20).
        clear_offset   (tuple)      : Offset for the clear search bar click. Defaults to (20, 10).
    """
    search_image_path = "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/vs-search.png"
    install_image_paths = [
        "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/vs-install-ext.png",
        "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/vs-install-ext-2.png"
    ]
    clear_image_path = "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/vs-clear-search.png"
    
    print(f"\nInstalling '{extension_name}'..")
    
    try:
        # Click on the Search bar in Extensions tab
        last_location = locate_and_click([search_image_path], offset=search_offset)
        
        if last_location:
            # Type the extension name in the search bar
            pyautogui.write(extension_name)
            sleep(3)
            
            # Click on the first search result
            pyautogui.click(last_location.left + 100, last_location.top + 100)
            
            # Click on the Install button
            locate_and_click(install_image_paths, offset=install_offset, sleep_time=3)
            
            # Clear the search bar
            locate_and_click([clear_image_path], offset=clear_offset)
            
            print(f"'{extension_name}' was Installed Successfully!")
    
    except pyautogui.ImageNotFoundException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Open VS Code
    open_vscode()

    # Give VS Code some time to open
    sleep(2)

    # Click on the Extensions tab
    locate_and_click(["/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/vs-extension.png"])

    # Get extension names from the user
    extensions = input("Enter the names of the vs extensions to install, separated by commas: ").split(',')

    # Convert each extension name to lowercase and trim whitespaces
    extensions = [ext.strip().lower() for ext in extensions]

    # Install each extension entered by the user
    for extension in extensions:
        install_extension(extension)
