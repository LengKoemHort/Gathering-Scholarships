"""
Django settings for social project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w3x-kor)$@_5w(9z26fmcj!_6q0*x%h58qs$*x@p_nr$_(fy!2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'social_django',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'corsheaders',
    'allauth.socialaccount.providers.google',
    'crispy_forms',
    'ScholarshipApp',
]
CORS_ORIGIN_ALLOW_ALL = True
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'social.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'social.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'scholarship_database',
        'USER':'root',
        'PASSWORD':'',
        'PORT':'3306',
        'HOST':'localhost',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        },
        'CONN_MAX_AGE': 600,
        'TEST': {
            'NAME': 'test_db',
        },
        'AUTOCOMMIT': True,
    }
}


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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'social/static'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1


SOCIALACCOUNT_PROVIDERS = {
     'google': {
         'SCOPE': [
             'profile',
             'email',
         ],
         'AUTH_PARAMS': {
             'access_type': 'online',
         }
     }
 }
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
        'SCOPE': ['email', 'public_profile'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'first_name',
            'last_name',
            'middle_name',
            'name',
            'name_format',
            'picture',
            'short_name'
        ],
        'EXCHANGE_TOKEN': True,
        # 'LOCALE_FUNC': 'path.to.callable',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v7.0',
    }
}

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'allauth.account.auth_backends.AuthenticationBackend',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'

ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'

ACCOUNT_EMAIL_REQUIRED = True

SOCIALACCOUNT_QUERY_EMAIL = True

ACCOUNT_SESSION_REMEMBER = True

