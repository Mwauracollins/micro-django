import os
import importlib


def migrate(app_name):
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, app_name)
    migrations_dir = os.path.join(app_dir, 'migrations')

    if not os.path.exists(migrations_dir):
        print(f"No migrations found for '{app_name}'")
        return

    # Get all migration files
    migration_files = sorted([f for f in os.listdir(migrations_dir) if f.endswith('.py') and f != '__init__.py'])

    for migration_file in migration_files:
        migration_module = importlib.import_module(f"{app_name}.migrations.{migration_file[:-3]}")
        migration = migration_module.Migration()

        for operation in migration.operations:
            if isinstance(operation, importlib.import_module('microdjango.db.migrations').CreateModel):
                print(f"Creating table for {operation.name}")

    print(f"Applied migrations for '{app_name}'")
