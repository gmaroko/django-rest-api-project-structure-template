from API.config.settings.base import *

DEBUG = env.bool('DJANGO_DEBUG', default=False)
SECRET_KEY = env('SECRET_KEY')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CORS_ORIGIN_ALLOW_ALL = True
SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = ['*']