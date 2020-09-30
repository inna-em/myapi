# Persons API

This API provides functionality for addind, updating and deleting user data.
Following methods are supported:

#### Jwt token endpoint
Method | Endpoint | Functionanlity
--- | --- | ---
POST | `/api-token-auth/` | Request jwt token

#### User Endpoints

Method | Endpoint | Functionality
--- | --- | ---
GET | `/api/v1/persons/` | List existing user ids
POST | `/api/v1/persons/` | Creates a user with provided name and surname
GET | `/api/v1/persons/<person_id>/` | Returns user name, surname and has_vector flag by id
PUT | `/api/v1/persons/` | Adds a serialized image to the user vecrot field
GET | `/api/v1/persons/compare/<person_id1>/<person_id2>/` | Returns euclidian distance between users' vectors
DELETE | `/api/v1/persons/<person_id>/` | Deletes a user

For launching the app follow the next steps.
First make sure you have installed virtualenv. If not, run this:

    $ pip install virtualenv
Then, Git clone this repo to your PC

    $ git clone https://github.com/inna-em/myapi.git
    $ cd myapi
Create a virtual environment

    $ virtualenv .venv && source .venv/bin/activate
Install django and django rest framework.

    $ pip install django
    $ pip install djangorestframework
Make migrations & migrate

    $ python manage.py makemigrations && python manage.py migrate
Create Super user
    
    $ python manage.py createsuperuser

Launch the app

    $ python manage.py runserver
