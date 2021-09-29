from .base import *

DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2', #Todos los datos de la base de datos POSTGRESQL
        'NAME': ('usersdb'),
        'USER': ('usersdb'),
        'PASSWORD': ('djangopass'),
        'HOST': ('localhost'),
        'PORT': ('5432'),
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')
