# Oscar Api Extension
this project is provides an endpoint for user registration which is not provided by Oscar Api

# Installation
After cloning cd into the project directory and install requirements using the `pip install requirements.txt` command. then proceed to run the project with the command `python manage.py runserver`. 

# Endpoints and Usage
there are two endpoints, one for creating users and the other for getting the list of all created users
# create User
 endpoint url : http://127.0.0.1:8000/api/register/
 parameters: first_name, last_name, email, password.
 request method: POST
 output: if successful, returns details without password and a status 201, else error message

# List all users
 endpoint url : http://127.0.0.1:8000/api/users/
 parameters: email and password.
 request method: GET
 output: returns a list of all users, with details such as name, email and date joined