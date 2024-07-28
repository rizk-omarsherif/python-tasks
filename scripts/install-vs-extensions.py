"""
Script Name         : install-vs-extensions.py
Script Description  : Automates the installation of VS Code extensions using PyAutoGUI, with an added PySide6 GUI for enhanced user-friendliness.

Author  : Omar Rizk
Course  : Python Programming
Diploma : Embedded Linux Diploma (Under Supervision of Eng. Moatasem Elsayed)
"""

import pyautogui
import subprocess
from time import sleep
import os
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = '/usr/lib/x86_64-linux-gnu/qt6/plugins'

def open_vscode():
    """
    Function to open Visual Studio Code using the 'code' command.
    """
    try:
        # Run the command that opens VS Code
        subprocess.run(["code"], check=True)
        log_output.append("VS Code opened successfully.")
        QApplication.processEvents()
    except FileNotFoundError:
        log_output.append("VS Code command 'code' not found. Make sure VS Code is installed and added to your PATH.")
        QApplication.processEvents()
    except subprocess.CalledProcessError as e:
        log_output.append(f"Failed to open VS Code. Error: {e}")
        QApplication.processEvents()

def locate_and_click(image_paths, confidence=0.85, offset=(0, 0), sleep_time=1, retries=3):
    """
    Function to locate an image on the screen and click on it.

    Args:
        image_paths (list)             : List of paths to the images to locate on the screen.
        confidence  (float , optional) : Confidence level for image recognition. Defaults to 0.85.
        offset      (tuple , optional) : Tuple (x, y) for adjusting the click position. Defaults to (0, 0).
        sleep_time  (int   , optional) : Time to sleep after clicking. Defaults to 1.
        retries     (int   , optional) : Number of times to retry locating the image. Defaults to 3.

    Returns:
        None
    """
    
    for image_path in image_paths:
        # Extract the image name from the path for print statements
        image_name = os.path.basename(image_path)  
        
        location = None   # Initialize the location to None
        attempt  = 0      # Initialize the attempt counter
        
        while location is None and attempt < retries:
            try:
                # Attempt to locate the image on the screen with the specified confidence
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                
                if location:
                    # If the image is found, print its location and prepare to click
                    ##log_output.append(f"\nFound '{image_name}' at location = {location}\nClicking now...")
                    
                    # Remove the file extension by splitting at the period and taking the first part
                    name_without_extension = image_name.split('.')[0]
                    # Split the name at the hyphen if it exists, otherwise keep it as a single part
                    parts = name_without_extension.split('-')
                    # Process the parts to remove digits
                    cleaned_parts = [''.join([char for char in part if not char.isdigit()]) for part in parts]
                    # Combine the cleaned parts with a space
                    status = ' '.join(cleaned_parts)
                    
                    log_output.append(f"\n{status}...")
                    QApplication.processEvents()
                else:
                    # If the image is not found, print a retry message and sleep for a while before retrying
                    log_output.append(f"\nAction in progress. Please wait... (Retry {attempt + 1} of {retries})")
                    QApplication.processEvents()
                    sleep(1)
                    
            except pyautogui.ImageNotFoundException:
                # Handle the case where the image is not found due to an exception
                log_output.append(f"\nAction in progress. Please wait... (Retry {attempt + 1} of {retries})")
                QApplication.processEvents()
                sleep(1)
                
            attempt += 1  # Increment the attempt counter
            
        if location:
            # If the location is found, click on the image with the specified offset
            pyautogui.click(location.left + offset[0], location.top + offset[1])
            sleep(sleep_time)  # Sleep for the specified time after clicking
            return location  # Return the location where the image was found and clicked
    
    # If none of the images are found after all retries, print a failure message
    log_output.append(f"\nCould not locate any of the icons on screen after {retries} attempts each.")
    QApplication.processEvents()
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
    search_image_path = "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/Searching.png"
    install_image_paths = [
        "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/Installing.png",
        "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/Installing2.png"
    ]
    clear_image_path = "/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/Clearing-Search.png"
    
    log_output.append(f"\nInstalling '{extension_name}'..")
    QApplication.processEvents()
    
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
            
            log_output.append(f"\n'{extension_name}' was Installed Successfully!")
            QApplication.processEvents()
    
    except pyautogui.ImageNotFoundException as e:
        log_output.append(f"Error: {e}")
        QApplication.processEvents()

def start_installation():
        
    extensions = input_field.text().split(',')
    # Convert each extension name to lowercase and trim whitespaces
    extensions = [ext.strip().lower() for ext in extensions]
    
    # Open VS Codex 
    open_vscode()
    
    # Give VS Code some time to open
    sleep(5)

    # Click on the Extensions tab
    locate_and_click(["/home/rizk/Desktop/my-repos/python-tasks/tasks/pyautogui-pics/Opening-Extensions-Tab.png"])

    # Install each extension entered by the user
    for extension in extensions:
        install_extension(extension)
        if extension == extensions[-1]:
            log_output.append(f"\n=========================================\n All Extensions were installed successfully!\nYou can exit now..")
            QApplication.processEvents()

if __name__ == "__main__":
    # PySide6 GUI
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("VS Code Extension Installer")

    layout = QVBoxLayout()

    label = QLabel("Enter the names of the VS Code extensions to install, separated by commas:")
    layout.addWidget(label)

    input_field = QLineEdit()
    layout.addWidget(input_field)

    log_output = QTextEdit()
    log_output.setReadOnly(True)
    layout.addWidget(log_output)

    install_button = QPushButton("Install Extensions")
    install_button.clicked.connect(start_installation)
    layout.addWidget(install_button)

    window.setLayout(layout)
    window.show()

    sys.exit(app.exec())
