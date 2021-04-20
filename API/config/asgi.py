import os

from django.core.asgi import get_asgi_application

# change this to production when deploying
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'API.config.settings.local')

application = get_asgi_application()
