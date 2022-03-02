# Flashcards

A web-based application for studying foreign vocabulary and phrases with user made flash cards. Built with Django and Vue.js. New words/phrases can be added via the Django admin. Flashcards can be filtered by topic and syntax.

## Getting Started

Prior knowledge of Python virtual environments, Django's admin and manage.py are recommended. These instructions assume a unix-like environment (Linux, MacOS).

### Prerequisites

Python3.6 or higher.

### Installing

Copy the project to your local machine. From the project root directory, open a terminal and create a virtual environment by running:

```
python -m venv venv
```

Once complete, activate the virtual environment by running:

```
. venv/bin/activate
```

To install project dependencies run:

```
pip install -r requirements.txt
```

Finally, create the database by running:

```
python manage.py migrate
```

You can now start the development server by running:

```
python manage.py runserver
```

And following the directions in the terminal. To add a new admin user, stop the development server and run the command:

```
python manage.py createsuperuser
```

Follow the terminal prompts. Use this user to access the Django admin at /admin/login. You can add words and topics via the admin interface.

## Running the tests

There are no tests at this time

## Deployment

This application is not currently intended for use outside of a local development environment. However, since it's built using Dango, it should be fairly easy to deploy the application to a sever. See the Django documentation for more details on deployment.

## Built With

* [Python](https://www.python.org/) - Language interpreter
* [Django](https://www.djangoproject.com/) - Web framework
* [Vue.js](https://vuejs.org/) - JS SPA Library

## Authors

* **st003** - *Initial work*
