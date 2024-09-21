import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'secret-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'project_name',
]

ROOT_URLCONF = 'project_name.urls'

WSGI_APPLICATION = 'project_name.wsgi.application'