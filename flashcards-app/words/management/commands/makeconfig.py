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

        self.config_allowed_hosts: list[str] = []
        if not self.config_debug:
            # TODO - add support for entering multiple values
            allowed_host: str = input('Enter allowed host: ')
            self.config_allowed_hosts.append(allowed_host)

        config: dict = {
            'databases': {
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME': f'{BASE_DIR}/db.sqlite3',
                }
            },
            'debug': self.config_debug,
            'allowedHosts': self.config_allowed_hosts,
            'requestWordHistoryMax': 15,
            'secretKey': get_random_secret_key()
        }

        with open(f'{BASE_DIR}/config.yml', 'w', newline='') as config_yaml:
            yaml.dump(config, config_yaml)

        self.stdout.write('Done. See configurations in \'config.yml\'')
