import os
import importlib
import sqlite3
from microdjango.db.models import Model

def migrate(app_name):
    migrations_dir = os.path.join(os.getcwd(), app_name, 'migrations')
    if not os.path.exists(migrations_dir):
        print(f"No migrations found for app '{app_name}'.")
        return

    migration_files = sorted([f for f in os.listdir(migrations_dir) if f.endswith('.py') and f != '__init__.py'])

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    for migration_file in migration_files:
        print(f"Applying migration: {migration_file}")
        module_name = f"{app_name}.migrations.{migration_file[:-3]}"
        migration_module = importlib.import_module(module_name)
        
        if hasattr(migration_module, 'Migration'):
            migration = migration_module.Migration()
            for operation in migration.operations:
                if isinstance(operation, dict) and 'model' in operation:
                    model_name = operation['model']
                    model_module = importlib.import_module(f"{app_name}.models")
                    model_class = getattr(model_module, model_name)
                    if issubclass(model_class, Model):
                        model_class.create_table(cursor)
                        print(f"Created table for model: {model_name}")

    conn.commit()
    conn.close()
    print("Migrations applied successfully.")