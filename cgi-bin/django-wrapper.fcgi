#!/home/u31975/python/bin/python
# -*- coding: utf-8 -*-
import sys, os

# Add a custom Python path.
sys.path.insert(0, "/home/u31975/xn---72-5cdabald9cyacceo4ba4afdoov1t.xn--p1ai/tg")

# Switch to the directory of your project. (Optional.)
# os.chdir("/home/u31975/xn---72-5cdabald9cyacceo4ba4afdoov1t.xn--p1ai/tg")

# Set the DJANGO_SETTINGS_MODULE environment variable.
os.environ['DJANGO_SETTINGS_MODULE'] = "settings"

from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="prefork", daemonize="false",
    minspare=1, maxspare=1, maxchildren=1)