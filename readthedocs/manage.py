#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.sqlite")
    sys.path.append(os.getcwd())
    sys.path.append(os.path.join(os.getcwd(), 'readthedocs'))
    os.environ['PATH'] = str(os.pathsep).join([
        os.path.join(os.getcwd(), 'node_modules', '.bin'),
        os.environ['PATH']])

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
