#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('MICRODJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from microdjango.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import MicroDjango. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
