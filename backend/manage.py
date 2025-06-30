#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # ...existing error handling...
        raise
    
    # Add port argument if not provided
    if len(sys.argv) == 2 and sys.argv[1] == 'runserver':
        sys.argv.append('0.0.0.0:3001')
    elif len(sys.argv) == 1:
        sys.argv.extend(['runserver', '0.0.0.0:3001'])
    
    execute_from_command_line(sys.argv)
