"""
WSGI config for test_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

# Also import sys and site to help enable virtualenv
import os, sys, site

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO_DIR = os.path.dirname(BASE_DIR)

# Add the site packages, to override any system-wide packages
site.addsitedir(os.path.join(REPO_DIR, '.env/lib/python3.5/site-packages'))

# As is
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dfb.settings")

# Calculate the path based on the location of the WSGI script
project = BASE_DIR
workspace = os.path.dirname(project)
sys.path.append(workspace)

sys.path = [REPO_DIR, os.path.dirname(REPO_DIR)] + sys.path
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
