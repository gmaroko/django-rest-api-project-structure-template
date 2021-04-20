from API.config.settings.base import *

DEBUG = env.bool('DJANGO_DEBUG', default=True)
SECRET_KEY = env('SECRET_KEY', default='c3q*hbhwpb9&0c2q*hbhwpb9&0c2q*hbhwpb9&0c2q*hbhwpb9&0c2q*hbhwpb9&0c2q*hbhwpb9&0c2q*hbhwpb9&0kv31et%ac')
ALLOWED_HOSTS = ['*']