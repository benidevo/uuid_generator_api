# UUID Generator API

## Description
This is a simple API that returns a key-value pair of randomly generated UUID. The key will be a timestamp and value will be a UUID. While the server is running, whenever the API is called, it returns all the previously generated UUIDs alongside a new UUID, with the newly generated UUID at the top.

- [Live Preview](https://documenter.getpostman.com/view/15138887/UVXkmZuX)

![Screenshot](uuidgen.png?raw=true "screenshot")
## Technologies 

The following technologies were used in this project:

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Heroku](https://www.heroku.com/)


## Requirements

Before starting, you need to have [Python](https://www.python.org/) installed on your computer.

Kindly ensure that you are in the root directory before running the following commands.

## Create a virtual environment

    python3 -m venv env

## Activate the virtual environment

    source env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate
## Run tests

    python manage.py test

## Start server

    python manage.py runserver
