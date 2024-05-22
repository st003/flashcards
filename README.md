# Flashcards

A web-based application for studying foreign vocabulary and phrases with user made flash cards. Built with Django, Django REST Framework, and Vue.js. New words/phrases can be added via the Django admin. Flashcards can be filtered by topic and syntax.

## Getting Started

Prior knowledge of Python virtual environments, Django's admin, and manage.py are required. These instructions assume a unix-like environment (Linux, MacOS).

### Prerequisites

Python3.8+

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

Next, make a copy of config.template and rename it to config.ini. This is your config file. You can now start the development server by running:

```
python manage.py runserver
```

and following the directions in the terminal. To add a new admin user, stop the development server and run the command:

```
python manage.py createsuperuser
```

Follow the terminal prompts. Use this user to access the Django admin at /admin/login. You can add words and topics via the admin interface.

## Running the tests

While the virtual environment is active, run:

```
python manage.py test
```

## Deployment

The following section details deployment of this app using Nginx + Gunicorn. For alternative approaches, see: [https://docs.djangoproject.com/en/4.2/howto/deployment/](https://docs.djangoproject.com/en/4.2/howto/deployment/).

### Static Files

After installing the source files, start the virtual environment, and run the command:

```
python manage.py collectstatic
```

This will copy all static files from all apps into a directory called "static/" in the application root directory.

### Nginx Configuration

Create a nginx conf file with the following values:

```
server {
    server_name <url>;

    location /static/ {
        root /path/to/application/;
        autoindex off;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/path/to/application/<socket-file-name>.sock;
    }
}
```

Reload your Nginx settings:

```
sudo systemctl reload nginx
```

### Systemd Service

Create a Systemd service file with the following values:

```
[Unit]
Description=Gunicorn daemon for <application-name> app
After=network.target

[Service]
User=<user>
Group=nginx
WorkingDirectory=/path/to/application
ExecStart=/path/to/application/venv/bin/gunicorn -w 1 -t 120 -b unix:/path/to/application/<socket-file-name>.sock -m 007 flashcards.wsgi

[Install]
WantedBy=multi-user.target
```

Start and enable your service

```
sudo systemctl start <service-file-name>.service
sudo systemctl enable <service-file-name>.service
```

## Built With

* [Python](https://www.python.org/) - Language interpreter
* [Django](https://www.djangoproject.com/) - Python Web-Application framework
* [Django REST Framework](https://www.django-rest-framework.org/) - REST API framework for Django
* [Vue.js](https://vuejs.org/) - JavaScript Single Page Application (SPA) framework

## Authors

* **st003** - *Initial work*
