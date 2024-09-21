import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'secret-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'core',
    'portfolio',
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'
