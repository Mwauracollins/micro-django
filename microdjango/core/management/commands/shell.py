import code
import os
import sys
from importlib import import_module

def run_shell():
    # Set up the environment
    os.environ.setdefault('MICRODJANGO_SETTINGS_MODULE', 'core.settings')
    
    # Import necessary modules
    from microdjango.db import models
    from microdjango.core.handlers import MicroDjango
    
    # Load the project's settings
    settings_module = os.environ['MICRODJANGO_SETTINGS_MODULE']
    settings = import_module(settings_module)
    
    # Load all models from installed apps
    for app in settings.INSTALLED_APPS:
        try:
            models_module = import_module(f'{app}.models')
            for name in dir(models_module):
                item = getattr(models_module, name)
                if isinstance(item, type) and issubclass(item, models.Model) and item is not models.Model:
                    globals()[name] = item
        except ImportError:
            pass
    
    # Set up a dict with local variables for the interactive shell
    context = globals().copy()
    context.update({
        'settings': settings,
        'MicroDjango': MicroDjango,
    })
    
    # Start the interactive shell
    code.interact(local=context, banner="Welcome to the MicroDjango interactive shell!")

if __name__ == '__main__':
    run_shell()
