#!/usr/bin/env python
from django.core.management import execute_manager
try:
    import settings # Assumed to be in the same directory.
except ImportError:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings)
    from common.appenginepatch.aecmd import setup_env
    setup_env(manage_py_env=True)

    # Recompile translation files
    from mediautils.compilemessages import updatemessages
    updatemessages()

    # Generate compressed media files for manage.py update
    import sys
    from mediautils.generatemedia import updatemedia
    if len(sys.argv) >= 2 and sys.argv[1] == 'update':
        updatemedia(True)