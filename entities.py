import json
from files import read, update

def file_log(func):
    def wrapper(*args, **kwargs):
        file_name = "activity.log"
        content = "User saved\n"

        # Execute the decorated function
        func(*args, **kwargs)

        # File handling
        try:
            with open(file_name, "r") as file:
                pass  # File exists, no need to create a new one
        except FileNotFoundError:
            with open(file_name, "w") as file:
                file.write("")  # Create an empty file if it does not exist

        # Update the file with content
        with open(file_name, "a") as file:
            file.write(content)
    
    return wrapper

def console_log(func):
    def wrapper(*args, **kwargs):
        isinstance = args[0]
        func(*args, **kwargs)  # Call the decorated function with unpacked arguments
        print(f"{isinstance.class_name} saved")    # Message after executing the decorated function
    return wrapper

def decorator1(func):
    def wrapper(*args, **kwargs):
        print("Step 1") 
        func(*args, **kwargs)
        print("Final step")
    return wrapper

class User:
    class_name = "User"

    def __init__(self, username, first_name, last_name, password=None, age=None, email=None):
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
    
    def __repr__(self):
        instance = f"{self.first_name} {self.last_name} ({self.username})"
        return f"<User: {instance}>"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @console_log
    def save(self):
        # Read existing data from users.json
        try:
            users = read("users.json")
        except FileNotFoundError:
            users = []

        # Check if the user already exists
        if not any(user['username'] == self.username for user in users):
            users.append(self.as_dict())
            update("users.json", users)

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
        # Read existing data from posts.json
        try:
            posts = read("posts.json")
        except FileNotFoundError:
            posts = []

        # Check if the post already exists
        if not any(post['title'] == self.title for post in posts):
            posts.append(self.as_dict())
            update("posts.json", posts)

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
        # Read existing data from articles.json
        try:
            articles = read("articles.json")
        except FileNotFoundError:
            articles = []

        # Check if the article already exists
        if not any(article['title'] == self.title for article in articles):
            articles.append(self.as_dict())
            update("articles.json", articles)
