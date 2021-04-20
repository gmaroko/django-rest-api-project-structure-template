import os

from django.core.wsgi import get_wsgi_application

# change this to production when deploying
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.config.settings.local')

application = get_wsgi_application()
