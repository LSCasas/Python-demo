"""File management"""
import json
import os


def create(file_name: str, content: list | dict = None) -> None:
    # Define a function 'create' that takes a file name and optional content (list or dict)

    """Create a new json file

    Args:
        file_name (str): File name or path
        content (str, optional): Text file content. Defaults to None.
    """

    # If content is provided, use write mode ("w"); otherwise, use exclusive creation mode ("x")
    mode = "w" if content else "x"

    try:
        # Try to open the file with the selected mode
        file = open(file_name, mode)

    except FileExistsError as error:
        # If file already exists and mode is "x", raise a custom error
        raise OSError(f"File '{file_name}' already exists") from error

    except PermissionError as error:
        # If there's no permission to create/write the file, raise a custom error
        raise OSError(f"You do not hav permisson to create '{file_name}'") from error

    # If content exists and is a list or dictionary
    if content and isinstance(content, (list, dict)):
        # If it's a dictionary, convert it to a single-element list
        if isinstance(content, dict):
            content = [content]

        # Convert the list or dict to a JSON-formatted string with indentation
        content = json.dumps(content, indent=2)

        # Write the JSON string into the file
        file.write(content)

    # Close the file to finish writing and free resources
    file.close()



def update(file_name: str, content: list | dict) -> None:
    # Define a function 'update' that takes a file name and content (list or dict)

    """Updates an existing file

    Args:
        file_name (str): File name or path
        content (str): Text file content
        overwrite (bool, optional): If True, file will be overwritten. Defaults to False.
    """

    # Check if content is not a valid list or dict, or is an empty string; if so, raise an error
    if not isinstance(content, dict | list) or content == "":
        raise ValueError("'content' argument must be specified")

    # Open the existing file in read mode
    file = open(file_name)

    # Read the content of the file and parse it from JSON format
    file_content = json.loads(file.read())

    # Close the file after reading
    file.close()

    # If the current content of the file is a list
    if isinstance(file_content, list):
        # If the new content is a dict, append it to the list
        if isinstance(content, dict):
            file_content.append(content)

        # If the new content is also a list, extend the list
        elif isinstance(content, list):
            file_content += content

    # If the current content of the file is a dict
    elif isinstance(file_content, dict):
        # If the new content is a dict, convert both to a list
        if isinstance(content, dict):
            file_content = [file_content, content]

        # If the new content is a list, add the existing dict at the beginning of the list
        elif isinstance(content, list):
            file_content = [file_content] + content

    # Open the file in write mode to overwrite it
    file = open(file_name, "w")

    # Write the updated content back to the file in JSON format
    file.write(json.dumps(file_content))

    # Close the file to save changes and free resources
    file.close()


def read(file_name: str) -> list | dict:
    # Define a function 'read' that takes a file name and returns its content as a list or dictionary

    """Returns the content of a text file

    Args:
        file_name (str): File name or path

    Returns(str): File content
    """

    # Check if the file exists; if not, raise a FileNotFoundError
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} was not found")

    # Open the file in read mode
    file = open(file_name)

    # Read the entire content of the file as a string
    content = file.read()

    # Close the file after reading
    file.close()

    # Convert the JSON string to a Python list or dictionary and return it
    return json.loads(content)

    """Returns the content of a text file

    Args:
        file_name (str): File name or path

    Returns(str): File content
    """
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"File {file_name} was not found")

    file = open(file_name)
    content = file.read()

    file.close()
    return json.loads(content)