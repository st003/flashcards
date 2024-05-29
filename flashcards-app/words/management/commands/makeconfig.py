import getpass
import os.path

import yaml

from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key

from flashcards.settings import BASE_DIR

class Command(BaseCommand):

    help: str = 'Create a new config file'

    def handle(self, *args, **options) -> None:

        if os.path.isfile(f'{BASE_DIR}/config.yml'):
            while True:
                proceed: str = input('A config file already exists. This operation will overwrite existing configurations. Do you wish to proceed? (Y/N): ')
                if proceed.upper() == 'Y':
                    break
                elif proceed.upper() == 'N':
                    self.stdout.write('Exiting makeconfig...')
                    return
                else:
                    self.stdout.write('Input not recognized')

        # debug mode
        while True:
            debug_setting: str = input('Configure for debug mode (T/F): ')
            if debug_setting.upper() == 'T':
                self.config_debug: bool = True
                break
            elif debug_setting.upper() == 'F':
                self.config_debug: bool = False
                break
            else:
                self.stdout.write('Input not recognized')

        # databases
        self.config_databases: dict = {
            'default': {}
        }

        self.stdout.write('Available database engines:')
        self.stdout.write('1. SQLite3')
        self.stdout.write('2. PostgreSQL')
        while True:
            database_type: str = input('Which database engine will you use? Enter number: ')

            if database_type == '1':
                self.config_databases['default'] = {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': f'{BASE_DIR}/db.sqlite3',
                }
                break

            elif database_type == '2':
                db_host: str = input('Enter database host (leave blank for localhost): ')
                db_name: str = input('Enter database name: ')
                db_user: str = input('Enter database user: ')
                db_password: str = getpass.getpass('Enter database password: ')

                self.config_databases['default'] = {
                    'ENGINE': 'django.db.backends.postgresql',
                    'HOST': db_host,
                    'PORT': 5432, # PostgreSQL default
                    'NAME': db_name,
                    'USER': db_user,
                    'PASSWORD': db_password,
                }
                break

            else:
                self.stdout.write('Input not recognized')

        # allowed hosts
        self.config_allowed_hosts: list[str] = []
        if not self.config_debug:
            # TODO - add support for entering multiple values
            allowed_host: str = input('Enter allowed host: ')
            self.config_allowed_hosts.append(allowed_host)

        config: dict = {
            'databases': self.config_databases,
            'debug': self.config_debug,
            'allowedHosts': self.config_allowed_hosts,
            'requestWordHistoryMax': 15,
            'secretKey': get_random_secret_key()
        }

        with open(f'{BASE_DIR}/config.yml', 'w', newline='') as config_yaml:
            yaml.dump(config, config_yaml)

        self.stdout.write('Done. See configurations in \'config.yml\'')
