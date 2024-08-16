# staging.py

from .base import *

DEBUG = False


# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# STATIC_URL = '/static/'


ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['your-staging-domain.com'])