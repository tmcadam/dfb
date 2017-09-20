"""
This is a django-split-settings main file.
For more information read this:
https://github.com/sobolevn/django-split-settings
Default environment is `developement`.
To change settings file:
`DJANGO_ENV=production python manage.py runserver`
"""
from split_settings.tools import optional, include
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def get_environment_file_path():
    return os.path.join(BASE_DIR, "ENVIRONMENT.cfg")


def get_environment_variable(file_name):
    with open(file_name) as f:
        environment = f.readline().replace('\r', '').replace('\n', '')
    return environment

ENVIRONMENT = get_environment_variable(get_environment_file_path())

base_settings = [
    'components/base.py',           # standard django settings
    # 'components/database.py',     # postgres
    # 'components/rq.py',           # redis and redis-queue
    # 'components/emails.py',       # smtp
    # 'components/*.py'             # You can even use glob
    'environments/{}.py'.format(ENVIRONMENT),   # Select the right env
    # optional('environments/local.py')         # Optionally override some settings
]

# Include settings:
include(*base_settings)
