def create_file(file_name: str, content=None):
    mode = "w" if content else "x"
    try:
        file = open(file_name, mode)
    except FileExistsError as error:
        raise IOError(f"File '{file_name}' already exists") from error
    except PermissionError as error:
        raise IOError(f"You dont have permission to create '{file_name}'") from error
    if content:
        file.write(content)
    file.close()



def modify_file(file_name, content: str, overwrite=False):
    # Validar que el contenido sea una cadena no vacía
    if not isinstance(content, str) or content == "":
        raise ValueError("content argument must be specified and should not be empty")
    
    # Elegir el modo de apertura del archivo
    mode = "w" if overwrite else "a"
    
    # Abrir el archivo con 'with' para asegurar el cierre adecuado
    with open(file_name, mode) as file:
        file.write(content)