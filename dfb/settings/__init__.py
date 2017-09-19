import os
from .base import BASE_DIR

file_name = os.path.join(BASE_DIR, "ENVIRONMENT.cfg")
with open(file_name) as f:
    ENVIRONMENT = f.readline()

if ENVIRONMENT == 'staging':
    from .staging import *
elif ENVIRONMENT == 'production':
    from .production import *
elif ENVIRONMENT == 'ci':
    from .production import *
elif ENVIRONMENT == 'development':
    from .development import *
