"""
Django settings for pushups project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from datetime import timedelta
# import djcelery
# djcelery.setup()
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#-2+byiet=(7dd^k%*8=q%v^h^q)2ac+$)6i#@imx87vvxgxoo'
TWILIO_ACCOUNT_SID='AC1228449546e2367b274cc342487419dc'
TWILIO_AUTH_TOKEN='b34cee3d99af7233b9e81dd885ad1e57'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True
TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'pushups/templates')]

ALLOWED_HOSTS = ['*']

CELERY_RESULT_BACKEND=os.environ['REDIS_URL']
BROKER_URL=os.environ['REDIS_URL']
# CELERY_RESULT_BACKEND=('djcelery.backends.database:DatabaseBackend', 'djcelery.backends.cache:CacheBackend',)
# BROKER_URL = 'django://'
# CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_twilio',
    'main',
    'userprofile',
    'phonenumber_field',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pushups.urls'

WSGI_APPLICATION = 'pushups.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases


# DATABASES = {
    # 'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pushups',                      # Or path to database file if using sqlite3.
        'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'pushups.celery.test_sms',
        'schedule': timedelta(seconds=30),
        'args': ()
    },
}

CELERY_TIMEZONE = 'UTC'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(PROJECT_PATH, 'static')]
AUTH_PROFILE_MODULE = 'userprofile.UserProfile'
