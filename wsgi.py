"""
WSGI config for test_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# Also import sys and site to help enable virtualenv
import os
import sys
import site
from django.core.wsgi import get_wsgi_application

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR = os.path.dirname(BASE_DIR)

# Add the site packages, to override any system-wide packages
site.addsitedir(os.path.join(BASE_DIR, '.env/lib/python3.5/site-packages'))

# As is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dfb.settings")

# Calculate the path based on the location of the WSGI script
project = BASE_DIR
workspace = os.path.dirname(project)
sys.path.append(BASE_DIR)

sys.path = [BASE_DIR, REPO_DIR, os.path.join(BASE_DIR, 'dfb')] + sys.path
application = get_wsgi_application()

