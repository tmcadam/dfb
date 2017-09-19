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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_name = os.path.join(BASE_DIR, "ENVIRONMENT.cfg")
with open(file_name) as f:
    ENVIRONMENT = f.readlines()[0].replace('\r', '').replace('\n', '')

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
