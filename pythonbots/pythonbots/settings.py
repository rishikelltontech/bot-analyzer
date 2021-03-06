"""
Django settings for pythonbots project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#import mongoengine 
# from mongoengine import register_connection
# register_connection(alias='default',name='logparsers')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'og4n(+r0#eqos_6#me)u16+rcy6c-r!1555uzbzn9#okgdjaoj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'readlog'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pythonbots.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pythonbots.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

#DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django_mongodb_engine',
#         'NAME' : 'logparsers',
#         'HOST' : '127.0.0.1',
#         'PORT' : '27017'
#     },
# }
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
        'NAME': 'botanalyzer',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/


STATIC_URL = '/static/'

#STATIC_ROOT = os.path.join(BASE_DIR, "static/")
#STATIC_ROOT = '/home/user/Downloads/HTC-tech-initiatives/shieldcon/static/'
#STATICFILES_DIRS = ( 'home/user/Downloads/HTC-tech-initiatives/shieldcon/static/', )
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
# MONGODB_USER = ''
# MONGODB_PASSWD = ''
# MONGODB_HOST = ''
# MONGODB_NAME = 'logparsers'
# MONGODB_DATABASE_HOST = \
#     'mongodb://%s:%s@%s/%s' \
#     % (MONGODB_USER, MONGODB_PASSWD, MONGODB_HOST, MONGODB_NAME)

# mongoengine.connect(MONGODB_NAME, host=MONGODB_DATABASE_HOST)