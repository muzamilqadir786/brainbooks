
"""
Django settings for fun project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/



For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import django_heroku

from .common import *

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cdwcsgx^d_2i+(#ec&b(x$ecq4wx@9(nvq%s!6dq%vyt+(^l=f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com']

INSTALLED_APPS += [
    'django_heroku'
]


WSGI_APPLICATION = 'brainbooks.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'd586ugq98avemg',
        'USER': 'ilxuiughrajugs',
        'PASSWORD': '66c33bcdb8d5af72b3e7b142ed0b74c2963e494121ef7619d4305e25399815e8',
        'HOST': 'ec2-52-200-215-149.compute-1.amazonaws.com',
        'PORT': '5432', #5432
    }
}

LOCAL_DEV = False #setting for different url patterns

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles' #Useless in development, no need to set it

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

django_heroku.settings(locals())
