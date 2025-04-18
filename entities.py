import json
import files

def file_log(func):
    # Define a decorator function called 'file_log' that takes another function as input

    def wrapper(*args, **kwargs):
        # Define the inner wrapper function that will wrap around the original function

        result = func(*args, **kwargs)
        # Call the original function with any arguments and store its result

        file_name = "activity.log"
        # Define the name of the log file

        content = "User saved\n"
        # Define the content to append to the log file

        try:
            # Try to open the log file in read mode to check if it exists
            with open(file_name, "r") as file:
                pass
        except FileNotFoundError:
            # If the file doesn't exist, create it by opening it in write mode
            with open(file_name, "w") as file:
                file.write("")

        # Open the file in append mode and write the log content
        with open(file_name, "a") as file:
            file.write(content)
        
        return result
        # Return the result of the original function call

    return wrapper
    # Return the wrapper function, completing the decorator


def console_log(func):
    # Define a decorator function called 'console_log' that takes another function as input

    def wrapper(*args, **kwargs):
        # Define the inner wrapper function that wraps the original function

        print("args:", args)
        # Print the positional arguments passed to the function

        print("kwargs:", kwargs)
        # Print the keyword arguments passed to the function

        func(*args, **kwargs)
        # Call the original function with the provided arguments

        print("User saved")
        # Print a message to the console after the function call

    return wrapper
    # Return the wrapper function, completing the decorator

def save_data(file_name, data):
    # Define a function 'save_data' that takes a file name and data to save

    try:
        # Try to read the existing content from the file
        content = files.read(file_name)

    except FileNotFoundError:
        # If the file doesn't exist, create it with the new data
        files.create(file_name, data)
        return data

    except json.JSONDecodeError:
        # If the file content is not valid JSON, recreate it with the new data
        files.create(file_name, data)
        return data

    # If the file exists and is valid JSON, update it with the new data
    files.update(file_name, data)

    # Return the data that was saved
    return data

class User:
    # Define a class 'User' with attributes for user details

    def __init__(self, username, name, last_name, password):
        # Initialize the attributes when a new User object is created
        self.username = username  # Assign the username
        self.name = name  # Assign the user's first name
        self.last_name = last_name  # Assign the user's last name
        self.password = password  # Assign the user's password

    def __str__(self) -> str:
        # Define the string representation of the User object
        # This will be called when you print the User object or use str() on it
        return f"{self.name} {self.last_name}"  # Returns the full name of the user

    @file_log
    @console_log
    def save(self):
        # Define a method 'save' that saves the user data
        file_name = "users.json"  # Set the file name where user data will be saved
        return save_data(file_name, self.__dict__)  # Save the user data as a dictionary and return the saved data


# class Post:
#     def __init__(self, title, content, status, created_by):
#         self.title = title
#         self.content = content
#         self.status = status
#         self.created_by = created_by

#     def as_dict(self):
#         return {
#             "title": self.title,
#             "content": self.content,
#             "status": self.status,
#             "created_by": self.created_by
#         }

#     @file_log
#     def save(self):
#         # Read existing data from posts.json
#         try:
#             posts = read("posts.json")
#         except FileNotFoundError:
#             posts = []

#         # Check if the post already exists
#         if not any(post['title'] == self.title for post in posts):
#             posts.append(self.as_dict())
#             update("posts.json", posts)

# class Article:
#     def __init__(self, title, content, status, image, created_by):
#         self.title = title
#         self.content = content
#         self.status = status
#         self.image = image
#         self.created_by = created_by

#     def as_dict(self):
#         return {
#             "title": self.title,
#             "content": self.content,
#             "status": self.status,
#             "image": self.image,
#             "created_by": self.created_by
#         }

#     @file_log
#     def save(self):
#         # Read existing data from articles.json
#         try:
#             articles = read("articles.json")
#         except FileNotFoundError:
#             articles = []

#         # Check if the article already exists
#         if not any(article['title'] == self.title for article in articles):
#             articles.append(self.as_dict())
#             update("articles.json", articles)
