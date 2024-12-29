import json
import os


def create(file_name: str, content: list | dict = None):
    mode = "w" if content else "x"
    try:
        with open(file_name, mode) as file:
            if content and isinstance(content, (list, dict)):
                content = json.dumps(content)  # Convertir a JSON
                file.write(content)
    except FileExistsError as error:
        raise IOError(f"File '{file_name}' already exists") from error
    except PermissionError as error:
        raise IOError(f"You don't have permission to create '{file_name}'") from error


def update(file_name, content: list | dict, overwrite=False):
    # Validar que el contenido sea una lista o un diccionario
    if not isinstance(content, (list, dict)):
        raise ValueError("content argument must be specified and should not be empty")
    
    # Leer el contenido actual del archivo
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

    # Escribir el contenido actualizado en el archivo
    with open(file_name, "w") as file:
        file.write(json.dumps(file_content))


def read(file_name: str):
    if not os.path.exists(file_name):
        return []  # Si el archivo no existe, devolver lista vacía
    
    with open(file_name, 'r') as file:
        content = file.read().strip()  # Usamos .strip() para eliminar espacios en blanco

    # Si el archivo está vacío, devolvemos una lista vacía
    if not content:
        return []

    return json.loads(content)
