import json
import os


def create(file_name: str, content: list | dict = None):
    mode = "w" if content else "x"
    try:
        with open(file_name, mode) as file:
            if content and isinstance(content, (list, dict)):
                content = json.dumps(content)  # Convert to JSON
                file.write(content)
    except FileExistsError as error:
        raise IOError(f"File '{file_name}' already exists") from error
    except PermissionError as error:
        raise IOError(f"You don't have permission to create '{file_name}'") from error


def update(file_name, content: list | dict, overwrite=False):
    # Validate that the content is a list or a dictionary
    if not isinstance(content, (list, dict)):
        raise ValueError("content argument must be specified and should not be empty")
    
    # Read the current content of the file
    try:
        file_content = read(file_name)
    except FileNotFoundError:
        file_content = []

    if isinstance(file_content, list):
        if isinstance(content, dict):
            file_content.append(content)
        elif isinstance(content, list):
            file_content += content

    elif isinstance(file_content, dict):
        if isinstance(content, dict):
            file_content = [file_content, content]
        elif isinstance(content, list):
            file_content = [file_content] + content

    # Write the updated content back to the file
    with open(file_name, "w") as file:
        file.write(json.dumps(file_content))


def read(file_name: str):
    if not os.path.exists(file_name):
        return []  # If the file doesn't exist, return an empty list
    
    with open(file_name, 'r') as file:
        content = file.read().strip()  # Use .strip() to remove whitespace

    # If the file is empty, return an empty list
    if not content:
        return []


    return json.loads(content)
