import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
file_name = os.path.join(BASE_DIR, "ENVIRONMENT.cfg")
with open(file_name) as f:
    ENVIRONMENT = f.readline()
print(ENVIRONMENT)
if ENVIRONMENT == 'staging':
    from dfb.env_settings.staging import *
elif ENVIRONMENT == 'production':
    from dfb.env_settings.production import *
elif ENVIRONMENT == 'ci':
    from dfb.env_settings.ci import *
elif ENVIRONMENT == 'development':
    from dfb.env_settings.development import *
print(SECRET_KEY)
