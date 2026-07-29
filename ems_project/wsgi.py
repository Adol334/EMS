"""
WSGI configuration for ems_project.

Exposes the WSGI application object for deployment.
"""

import os
from django.core.wsgi import get_wsgi_application

#Set the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ems_project.settings')

#Create the WSGI application instance
application = get_wsgi_application()