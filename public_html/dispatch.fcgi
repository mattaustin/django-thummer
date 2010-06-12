#!/usr/bin/python
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/var/www/thummer")

# Switch to the directory of your project. (Optional.)
os.chdir("/var/www/thummer/thummer")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "thummer.settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false", maxchildren=2, minspare=0, maxspare=1)
