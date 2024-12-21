import os
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Define the project name
project_name = "cnnClassifier" 

# List of files to be created
list_of_files = [
    "github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dav.yaml",
    "params.yaml",
    "requirement.txt",
    "setup.py",
    "research/trails.ipynb",
    "templets/index.html"
]

# Loop through each file and create directories and files
for filepath in list_of_files:
    filepath = Path(filepath)  # Convert the string filepath to a Path object
    filedir, filename = os.path.split(filepath)  # Split the file path into directory and filename

    try:
        # Check if directory exists, if not, create it
        if filedir != "":  # Avoid empty directory creation
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir} for the file: {filename}")

        # Check if the file exists or if it is empty
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            # Create an empty file if it does not exist or is empty
            with open(filepath, "w") as f:
                pass  # Create the file but don't add any content
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filename} already exists")

    except Exception as e:
        logging.error(f"Error creating file or directory {filepath}: {str(e)}")

