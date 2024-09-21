import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_(Sm>z$F%k-b9;caGc3YV[pdnQ7ha"P$I+}-vlaLr#&.fb)^/>'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'core',
    'portfolio'
]

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'