import files

def file_log(func):
    def wrapper(*args, **kwargs):
        file_name = "activity.log"
        content = "User saved\n"

        # Ejecutar la función decorada
        func(*args, **kwargs)

        # Manejo del archivo
        try:
            with open(file_name, "r") as file:
                pass  # Archivo existe, no es necesario crear uno nuevo
        except FileNotFoundError:
            with open(file_name, "w") as file:
                file.write("")  # Crear archivo vacío si no existe

        # Actualizar el archivo con contenido
        with open(file_name, "a") as file:
            file.write(content)
    
    return wrapper

def console_log(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)  # Llamar a la función decorada con los argumentos desempaquetados
        print("User saved")    # Mensaje después de ejecutar la función decorada
    return wrapper

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Paso 1") 
        func(*args, **kwargs)
        print("Paso al final")
    return wrapper

class User:
    def __init__(self, username, age, first_name, last_name, password=None, email=None):
        self.username = username
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email

    def as_dict(self):
        return {
            "username": self.username,
            "age": self.age,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password,
            "email": self.email
        }
    @file_log
    @console_log
    def save(self):
        # Leemos los datos existentes en users.json
        try:
            users = files.read("users.json")
        except FileNotFoundError:
            users = []

        # Verificar si el usuario ya existe
        if not any(user['username'] == self.username for user in users):
            users.append(self.as_dict())
            files.update("users.json", users)


class Post:
    def __init__(self, title, content, status, created_by):
        self.title = title
        self.content = content
        self.status = status
        self.created_by = created_by

    def as_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "status": self.status,
            "created_by": self.created_by
        }

    def save(self):
        # Leemos los datos existentes en posts.json
        try:
            posts = files.read("posts.json")
        except FileNotFoundError:
            posts = []

        # Verificar si el post ya existe
        if not any(post['title'] == self.title for post in posts):
            posts.append(self.as_dict())
            files.update("posts.json", posts)


class Article:
    def __init__(self, title, content, status, image, created_by):
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by

    def as_dict(self):
        return {
            "title": self.title,
            "content": self.content,
            "status": self.status,
            "image": self.image,
            "created_by": self.created_by
        }

    def save(self):
        # Leemos los datos existentes en articles.json
        try:
            articles = files.read("articles.json")
        except FileNotFoundError:
            articles = []

        # Verificar si el artículo ya existe
        if not any(article['title'] == self.title for article in articles):
            articles.append(self.as_dict())
            files.update("articles.json", articles)