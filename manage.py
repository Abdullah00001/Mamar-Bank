#!/usr/bin/env python
import os
import sys


def main():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mamarbank.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Get the port from the environment variable, default to 8000 if not set
    port = os.environ.get("PORT", "8000")

    # Replace the default runserver command line argument
    addrport = f"0.0.0.0:{port}"
    sys.argv = ["manage.py", "runserver", addrport]

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
