
import os
import shutil
from microdjango.conf import project_template


def startproject(project_name):
    target = os.path.join(os.getcwd(), project_name)
    if os.path.exists(target):
        print(f"Directory {project_name} already exists.")
        return

    template_dir = os.path.join(project_template.__path__[0])
    shutil.copytree(template_dir, target)

    # rename project directory
    os.rename(
        os.path.join(target, 'project_name'),
        os.path.join(target, project_name)
    )

    # update settings.py and manage.py with the project name
    settings_path = os.path.join(target, project_name, 'settings.py')
    manage_path = os.path.join(target, 'manage.py')

    for file_path in [settings_path, manage_path]:
        with open(file_path, 'r') as file:
            content = file.read()

        content = content.replace('project_name', project_name)

        with open(file_path, 'w') as file:
            file.write(content)

    print(f"Project '{project_name}' created successfully.")
