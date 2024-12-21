import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns its content as a ConfigBox object.

    Args:
        path_to_yaml (Path): Path to the YAML file.

    Raises:
        ValueError: If the YAML file is empty.
        Exception: For other errors.

    Returns:
        ConfigBox: Parsed YAML content.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except FileNotFoundError:
        raise ValueError(f"YAML file not found at {path_to_yaml}")
    except yaml.YAMLError:
        raise ValueError(f"Error in YAML parsing at {path_to_yaml}")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates a list of directories.

    Args:
        path_to_directories (list): List of paths to directories.
        verbose (bool): If True, log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """Saves data to a JSON file.

    Args:
        path (Path): Path to the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"JSON file saved at: {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """Loads data from a JSON file.

    Args:
        path (Path): Path to the JSON file.
        
    Returns:
        ConfigBox: Data loaded from the JSON file as attributes.
    """
    with open(path) as f:
        content = json.load(f)

    logger.info(f"JSON file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Saves data as a binary file.

    Args:
        data (Any): Data to be saved as binary.
        path (Path): Path to the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """Loads data from a binary file.

    Args:
        path (Path): Path to the binary file.
    
    Returns:
        Any: The object stored in the binary file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """Gets the size of a file in KB.

    Args:
        path (Path): Path of the file.
        
    Returns:
        str: File size in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"

def decodeImage(imgstring, filename):
    """Decodes a base64 image string and saves it to a file.

    Args:
        imgstring (str): Base64 encoded image string.
        filename (str): Output file name to save the image.
    """
    imgdata = base64.b64decode(imgstring)
    with open(filename, "wb") as f:
        f.write(imgdata)

def encodeImageIntoBase64(croppedImagePath):
    """Encodes an image file into a base64 string.

    Args:
        croppedImagePath (str): Path to the image to encode.

    Returns:
        str: Base64 encoded string of the image.
    """
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())  # Fix here: using base64.b64encode
