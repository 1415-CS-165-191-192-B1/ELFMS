#!/usr/bin/env python
"""
This is the main entry point for a Django application. All it really does is set
up the environment variables you need to get the app running. Our project is
called `twanger`, and it is a normal Python module (it has a __init__.py), and
it has a settings.py. Here we tell Django that we want to use that settings file
as the entry for our app. The rest is built into Django's internals. This script
ultimately just tells django where our configuration is and prints out or parses
all the commands that are issued from the command line.

Running manage on it's own should output something like:

09:51 $ ./manage.py
Usage: manage.py subcommand [options] [args]

Options:
  -v VERBOSITY, --verbosity=VERBOSITY
                        Verbosity level; 0=minimal output, 1=normal output,
                        2=verbose output, 3=very verbose output
  --settings=SETTINGS   The Python path to a settings module, e.g.
                        "myproject.settings.main". If this isn't provided, the
                        DJANGO_SETTINGS_MODULE environment variable will be
                        used.
  --pythonpath=PYTHONPATH
                        A directory to add to the Python path, e.g.
                        "/home/djangoprojects/myproject".
  --traceback           Raise on exception
  --version             show program's version number and exit
  -h, --help            show this help message and exit

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[django]
    check
    cleanup
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    runfcgi
    shell
    sql
    sqlall
    sqlclear
    sqlcustom
    sqldropindexes
    sqlflush
    sqlindexes
    sqlinitialdata
    sqlsequencereset
    startapp
    startproject
    syncdb
    test
    testserver
    validate

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

"""

import os
import sys

if __name__ == "__main__":
    # Sets the environment variable for the setting module IF it doesnt exist.
    # We can override it in the ENV if we want.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "twanger.settings")

    from django.core.management import execute_from_command_line

    # executes the command line interface for django using the above settings
    # module and accepts the arguments from the command line as a parameter.
    execute_from_command_line(sys.argv)
