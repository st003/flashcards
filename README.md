# Flashcards

A web-based application for studying foreign vocabulary and phrases with user made flash cards. Built with Django, Django REST Framework, and Vue.js. New words/phrases can be added via the Django admin. Flash cards can be filtered by topic and syntax.

## Getting Started

Prior knowledge of Django, Django REST Framework, and Vue.js is required. These instructions assume a unix-like environment (Linux, MacOS).

### Prerequisites

Python3.8+

### Installing

Copy the project to your local machine. From the flashcards-app directory, open a terminal and create a virtual environment by running:

```
python -m venv venv
```

Once complete, activate the virtual environment by running:

```
. venv/bin/activate
```

With the virtual environment active, install project dependencies by running the command:

```
pip install -r requirements.txt
```

Next, create the database by running:

```
python manage.py migrate
```

Next, generate a configuration file by running the command:

```
python manage.py makeconfig
```

Follow the prompts. To add a new admin user, run the command:

```
python manage.py createsuperuser
```

Follow the prompts. You can now start the development server by running:

```
python manage.py runserver
```

Use the admin user to access the Django admin in the browser at http://127.0.0.1:8000/admin/login. You can add words and topics via the admin interface.

## Running the tests

While the virtual environment is active, run the command:

```
python manage.py test
```

## Deployment

See DEPLOYMENT for deployment instructions using Linux/Nginx/Gunicorn. For alternative approaches, refer to the Django docs at: [https://docs.djangoproject.com/en/4.2/howto/deployment/](https://docs.djangoproject.com/en/4.2/howto/deployment/).


## Built With

* [Python](https://www.python.org/) - Language interpreter
* [Django](https://www.djangoproject.com/) - Python Web-Application framework
* [Django REST Framework](https://www.django-rest-framework.org/) - REST API framework for Django
* [Vue.js](https://vuejs.org/) - JavaScript Single Page Application (SPA) framework

## Authors

* **st003** - *Maintainer*
