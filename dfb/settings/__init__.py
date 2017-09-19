import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
file_name = os.path.join(BASE_DIR, "ENVIRONMENT.cfg")
with open(file_name) as f:
    ENVIRONMENT = f.readline()
print(ENVIRONMENT)

if ENVIRONMENT == 'staging':
    from dfb.settings.staging import *
elif ENVIRONMENT == 'production':
    from dfb.settings.production import *
elif ENVIRONMENT == 'ci':
    from dfb.settings.ci import *
elif ENVIRONMENT == 'development':
    from dfb.settings.development import *
