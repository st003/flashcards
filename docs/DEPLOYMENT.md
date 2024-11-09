# Deployment

This document details deployment instructions with an RPM-based Linux instance, Nginx, and Gunicorn. For alternative approaches, see refer to the Django docs at: [https://docs.djangoproject.com/en/4.2/howto/deployment/](https://docs.djangoproject.com/en/4.2/howto/deployment/).

## Goals

Deploying this application requires completing the following steps:

1. Configuring Linux
2. Installing Source Files
3. Application Configuration
5. Creating Systemd Service
4. Configuring Nginx

## Configuring Linux

Before installing a copy of the application, software and users need to be added the Linux instance. This guide does not cover firewall configuration, but your Linux server should have ports 80 and 443 open.

### Installing Nginx, Python, and Certbot

Install Nginx, Python, and Let's Encrypt's Certbot with the following command:

```
sudo dnf install nginx python3.8 python3-certbot-nginx
```

*Note: The Python version must be at least 3.8, but new versions are supported. Also, you may need to start and/or enable nginx in Systemd.*

TODO - finish this section

### Adding a User

Next we need to add a user without admin privileges under which the application will run. Example usernames include: webapps, production, development, etc. This guide will use 'production' for the username. To add a new user, use the command:

```
sudo adduser production
```

TODO - expand section to include instructions for the new user's home directory (or not)

Next, add the production user to the nginx group by running the command:

TODO - investigate if this is correct, or if it should be the other way around

```
sudo usermod -a -G nginx production
```

*Note: the 'a' means append the group(s) specified after the 'G'.*

## Installing Source Files

Pick a location to place the application files. Common options include in a directory in the production user's home directory or in the 'srv' directory in the linux file system root. This guide will install into a directory called 'flashcards1' under 'srv'.

*Note: from this point until configuring the Systemd service, it may be wise to switch to the production user so files and directories automatically aquire the production user and group.*

```
mkdir /srv/flashcards1
```

Copy the application files into the newly created directory. Navigate into the directory and create a Python virtual environment:

```
python -m venv venv
```

Activate the virtual environment with the command:

```
. venv/bin/activate
```

Install the required Python dependencies with the command:

```
pip install -r requirements.txt
```

Next, generate a configuration file by running the command:

```
python manage.py makeconfig
```

Follow the prompts. Now create the database by running:

```
python manage.py migrate
```

*Note for PostgreSQL: the version of psycopg included in requirements.txt may not be adequate for connecting to a PostgreSQL server. If you receive an exception with an error message similar to: 'No module named psycopg', try installing the binary version of psycopg with the command:*

```
pip install psycopg[binary]
```

To add a Django admin superuser, run the command:

```
python manage.py createsuperuser
```

Follow the terminal prompts.

### Static Files

Because there are static files for multiple 'Django apps', all static files need to be gathered into a unified location. With the virtual environment still running, run the command:

```
python manage.py collectstatic
```

This will collect all static files from all 'Django apps' and copy them into a newly created directory called 'staticfiles' in flashcards1. While running in production mode, Django does not server static files. They will instead be server by the Nginx server.

Exit the virtual environment with the command:

```
deactivate
```

*Note: at this point you may exit the production user. Always verify the user and group for the application files are production:production*

## Systemd Service

Next, we'll create a Systemd service file. Navigate to /etc/systemd/system and create a new file called 'flashcards1.service'. Set the contents of the new file to:

TODO - expand upon the meaning of these configurations

```
[Unit]
Description=Gunicorn daemon for flashcards1 app
After=network.target

[Service]
User=production
Group=nginx
WorkingDirectory=/srv/flashcards1
ExecStart=/srv/flashcards1/venv/bin/gunicorn -w 1 -t 120 -b unix:/srv/flashcards1/flashcards1.sock -m 007 flashcards.wsgi

[Install]
WantedBy=multi-user.target
```

Finally, start and enable your service with the commands:

```
sudo systemctl start flashcards1.service
sudo systemctl enable flashcards1.service
```

## Configuring Nginx

Next, we need to configure a Nginx virtual host and add configurations for the applications static files and also proxying traffic the gunicorn socket. In this guide, we are using the domain name 'flashcards1.example.com'. In the /etc/nginx/conf.d directory, create a new file called flashcards1.conf. Set the contents of the new file to:

TODO - expand on the meaning of each of these configuration settings

```
server {
    server_name flashcards1.example.com;

    location /static/ {
        root /srv/flashcards1/;
        autoindex off;
    }

    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host $http_host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/srv/flashcards1/flashcards1.sock;
    }
}
```

Reload your Nginx settings with the command:

```
sudo systemctl reload nginx
```

### Installing a TLS Certificate

Finally, install a TLS certificate by running the command:

```
sudo certbot --nginx
```

Follow the prompts to select the application's host name. Your site should now fully installed.

#### Automatic TLS Certificate Renewal

To schedule automatic renewal of Let's Encrypt TLS certificates, create a systemd service and timer. Create a new file called 'certbot-renew.service' with the contents:

```
[Unit]
Description=Renew certificates acquired via Certbot
Documentation=https://eff-certbot.readthedocs.io/en/stable/

[Service]
Type=oneshot
ExecStart=/usr/bin/certbot -q renew
PrivateTmp=true
```

Save this file into the systemd configuration directory, typically located in '/etc/systemd/system/'.

*Note: you may need to verify the correct path to certbot for your installation*

Then create a second file called 'certbot-renew.timer' with the contents:

```
[Unit]
Description=Run Certbot twice daily

[Timer]
OnCalendar=*-*-* 00/12:00:00
RandomizedDelaySec=12h
Persistent=true

[Install]
WantedBy=timers.target
```

Save this file into the systemd configuration directory as well. Finally start and enable the timer using the commands:

```
systemctl start certbot-renew.timer
systemctl enable certbot-renew.timer
```

Certbot will check for eligible renewals approximately every 12 hours.
