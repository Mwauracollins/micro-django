import os
from importlib import import_module


def makemigrations(app_name):
    current_dir = os.getcwd()
    app_dir = os.path.join(current_dir, app_name)

    if not os.path.exists(app_dir):
        print(f"App '{app_name}' does not exist.")
        return

    migrations_dir = os.path.join(app_dir, 'migrations')
    if not os.path.exists(migrations_dir):
        os.makedirs(migrations_dir)

    # Load models
    models_module = import_module(f"{app_name}.models")
    models = [getattr(models_module, name) for name in dir(models_module)
              if isinstance(getattr(models_module, name), type)
              and issubclass(getattr(models_module, name), import_module('microdjango.db.models').Model)
              and getattr(models_module, name) is not import_module('microdjango.db.models').Model]

    # Create file
    migration_number = len([f for f in os.listdir(migrations_dir) if f.endswith('.py') and f != '__init__.py'])
    migration_file = os.path.join(migrations_dir, f'{migration_number:04d}_auto.py')

    with open(migration_file, 'w') as f:
        f.write("from microdjango.db import migrations, models\n\n")
        f.write("class Migration(migrations.Migration):\n")
        f.write("    operations = [\n")
        for model in models:
            f.write(f"        migrations.CreateModel('{model.__name__}',\n")
            f.write("            fields={\n")
            for field_name, field in model.__dict__.items():
                if isinstance(field, import_module('microdjango.db.models').Field):
                    f.write(f"                '{field_name}': models.{field.__class__.__name__}(),\n")
            f.write("            },\n")
        f.write("    )]\n")

    print(f"Created migration for '{app_name}'")