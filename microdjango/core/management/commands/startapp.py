import os


def startapp(app_name):
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, app_name)

    if os.path.exists(app_dir):
        print(f"App '{app_name}' already exists.")
        return

    os.makedirs(app_dir)

    # Create app files TODO:create template for app files
    open(os.path.join(app_dir, '__init__.py'), 'w').close()

    with open(os.path.join(app_dir, 'models.py'), 'w') as f:
        f.write("from microdjango.db import models\n\n# Create your models here\n")

    with open(os.path.join(app_dir, 'views.py'), 'w') as f:
        f.write("from microdjango.http import HttpResponse\n\n# Create your views here\n")

    print(f"App '{app_name}' created successfully.")