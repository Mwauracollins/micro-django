import sys
import sqlite3
import os

from microdjango.core.management.commands import runserver, startproject
from microdjango.core.management.commands.makemigrations import makemigrations
from microdjango.core.management.commands.migrate import migrate
from microdjango.core.management.commands.startapp import startapp

DATABASE_NAME = 'db.sqlite3'


def create_database_if_not_exists():
    """Create the SQLite database if it doesn't exist."""
    if not os.path.exists(DATABASE_NAME):
        print(f"Creating SQLite database '{DATABASE_NAME}'...")
        conn = sqlite3.connect(DATABASE_NAME)
        conn.close()
    else:
        print(f"SQLite database '{DATABASE_NAME}' already exists.")


def execute_from_command_line(argv=None):
    """Run a management command from the command line."""

    if argv is None:
        argv = sys.argv

    if len(argv) < 2:
        print("Usage: manage.py <command> [<args>]")
        return

    command = argv[1]

    if command == 'runserver':
        runserver.run_server()

    elif command == 'startproject':
        project_name = argv[2] if len(argv) > 2 else 'myproject'
        startproject.startproject(project_name)

    elif command == 'startapp':
        if len(argv) < 3:
            print("Usage: python manage.py startapp <app_name>")
            return
        app_name = argv[2]
        startapp(app_name)

    elif command == 'makemigrations':
        app_name = argv[2] if len(argv) > 2 else None
        if app_name is None:
            print("Usage: python manage.py makemigrations <app_name>")
            return
        makemigrations(app_name)

    elif command == 'migrate':
        create_database_if_not_exists()

        app_name = argv[2] if len(argv) > 2 else None
        if app_name is None:
            print("Usage: python manage.py migrate <app_name>")
            return
        migrate(app_name)

    else:
        print(f"Unknown command: {command}")
        print("Available commands: runserver, startproject, startapp, makemigrations, migrate")
