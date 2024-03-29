"""
Django settings for socialnetwork project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
# import django_on_heroku
import django_heroku
from decouple import config 
import dj_database_url
load_dotenv()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY = os.getenv('SECRET_KEY')



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Application definition
AUTHENTICATION_BACKENDS = [
    
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    # ........
    # created these two apps
    'social',
    'landing',
    #
    # got the following from https://django-allauth.readthedocs.io/en/latest/installation.html
    # this is for login/register/etc  
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #
    # needed for our forms to look nicer 
    'crispy_forms',
    # 
    # ........
]

# got this from https://django-allauth.readthedocs.io/en/latest/installation.html
SITE_ID = 1
# 

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware', # added ... to help serve static files during production follow this link https://medium.com/@naufal.ihsan21/how-to-serve-static-files-in-django-using-whitenoise-cda11f9bb643 

]

ROOT_URLCONF = 'socialnetwork.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # this will lead to the templates folder within social network project
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

WSGI_APPLICATION = 'socialnetwork.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


db_from_env = dj_database_url.config(conn_max_age=500)            # added ... required for the dj_databse_url module
DATABASES['default'].update(db_from_env)                          # added ... required for the dj_databse_url module
                                                                  # https://pypi.org/project/django-database-url/



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


MEDIA_URL = '/media/'                                            # added ... created a media folder which will store our users images, videos, etc                       
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')                     # added the path ... so media is for users , static is for the coder who wants to uplaod images, videos, etc
                                                                 # go to base directory () access media folder 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static') 
]
STATIC_URL = '/static/'

STATICFILES_DIRS = [                                                              # added .. tells django where to look for static files besides in the apps 
    os.path.join(BASE_DIR, 'static'),                                             # we want django to look inside our static folder that we created 
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')                                # added this root for the staticfiles .. during production all static files are collected and dumped into staticfiles folder
                                                                                   # using the command .. python manage.py collectstatic .. will take all static files and create then dump them into staticfiles folder 
                                                                                   # go to base directory () access staticfiles folder 
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'    # added for Adding compression and caching support

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# .... needed for crispy templates
CRISPY_TEMPLATE_PACK = 'bootstrap4'
LOGIN_REDIRECT_URL = 'post-list'
ACCOUNT_EMAIL_REQUIRED = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#

# STATIC_URL = '/static/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
# django_on_heroku.settings(locals())    # added ... required for django heroku 
django_heroku.settings(locals())    # added ... required for django heroku 

