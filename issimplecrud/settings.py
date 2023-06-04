"""
Django settings for issimplecrud project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

import os
import dj_database_url
import environ

import cloudinary
import cloudinary.uploader
import cloudinary.api



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env()

environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'knox',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_framework_simplejwt.token_blacklist',
    'cloudinary',
    'database',
    'authentication',
    'profiles',
    'language',
    'workexp',
    'blogs',
    'payment',
    'availability',
    'chat',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':('knox.auth.TokenAuthentication',)
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'issimplecrud.urls'

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

WSGI_APPLICATION = 'issimplecrud.wsgi.application'



# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


'''DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',        
        conn_max_age=600    
    )
}'''

DATABASES = {
    'default' : dj_database_url.parse(env('DATABASE_URL'))
}



'''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wordly_tqqg',
        'USER': 'admin',
        'PASSWORD': 'HASXG96RTMKvdqH4myv6C7oENx3UKlLM',
        'HOST': 'dpg-cglms3hmbg56g47h5m4g-a.ohio-postgres.render.com',
        'PORT': '5432',
    }
}'''

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DATETIME_INPUT_FORMATS = (
            '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
            '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
            '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
            '%Y-%m-%d',              # '2006-10-25'
            '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
            '%m/%d/%Y',              # '10/25/2006'
            '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
            '%m/%d/%y %H:%M',        # '10/25/06 14:30'
            '%m/%d/%y',              # '10/25/06'
            '%m/%y'                  # '02/30'
                                            )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

if not DEBUG:
     STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
     STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'database.CustomUser'

#CORS_ALLOW_ALL_ORIGINS
#CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ['*']
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "https://wordly-zgzi.onrender.com",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
]
CORS_ORIGIN_WHITELIST = [
     "http://localhost:8080",
]

CORS_ALLOWED_ORIGINS = [
    "https://wordly-zgzi.onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://wordly-zgzi.onrender.com",
]

#Cloudinary - Django integration

cloudinary.config(
     
     cloud_name = "dy1a6wx8l",
     api_key = "738141884438293",
     api_secret = "jVFda0Zf8IAxhCApjHEBDmwRgCg",
)
