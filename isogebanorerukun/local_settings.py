import os

from isogebanorerukun2.isogebanorerukun2.settings import ALLOWED_HOSTS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = []

DEBUG = True