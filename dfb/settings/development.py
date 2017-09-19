from dfb.settings.base import *

INSTALLED_APPS += ['django_nose']
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
