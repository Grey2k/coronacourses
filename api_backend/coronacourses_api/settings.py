"""
Django settings for coronacourses_api project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import yaml

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Config loader
try:
    with open(os.path.join(BASE_DIR, "data", "config.yml"), "r") as _file:
        config = yaml.load(_file, Loader=yaml.SafeLoader)
except FileNotFoundError:
    config = {}

try:
    _conf_ccapi = config["ccAPI"]
except KeyError:
    _conf_ccapi = {}


def _get_conf(name: str, default: str = None):
    if ("CCAPI_" + name).upper() in os.environ:
        return os.environ[("CCAPI_" + name).upper()]
    elif name in _conf_ccapi:
        return _conf_ccapi[name]
    else:
        return default


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
if _get_conf("SecretKey") not in (None, "<INSERT-SECRET-KEY-HERE>"):
    SECRET_KEY = _get_conf("SecretKey")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(_get_conf("Debug")) if _get_conf("Debug") is not None else False

ALLOWED_HOSTS = _get_conf("AllowedHosts", ["*"])


# Application definition

INSTALLED_APPS = [
    "coronacourses_api.rest",
    'oauth2_provider',
    'rest_framework',
    "channels",
    "coronacourses_api.websocket",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coronacourses_api.urls'
ASGI_APPLICATION = "coronacourses_api.urls.application"
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(_get_conf("redisHost", "redis"), int(_get_conf("redisPort", 6379)))],
        },
    },
}

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

WSGI_APPLICATION = 'coronacourses_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
if _get_conf("dbType") in (None, "sqlite3"):
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': _get_conf("dbFile", os.path.join(BASE_DIR, "data", "db.sqlite3"))
        }
    }
elif _get_conf("dbType") == "mysql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': _get_conf("dbHost", ""),
            'PORT': _get_conf("dbPort", ""),
            'USER': _get_conf("dbUser", "ccapi"),
            'PASSWORD': _get_conf("dbPW", ""),
            'NAME': _get_conf("dbName", "ccapi")
        }
    }
elif _get_conf("dbType") == "postgresql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'HOST': _get_conf("dbHost", ""),
            'PORT': _get_conf("dbPort", ""),
            'USER': _get_conf("dbUser", "ccapi"),
            'PASSWORD': _get_conf("dbPW", ""),
            'NAME': _get_conf("dbName", "ccapi")
        }
    }
elif _get_conf("dbType") == "oracle":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.oracle',
            'HOST': _get_conf("dbHost", ""),
            'PORT': _get_conf("dbPort", ""),
            'USER': _get_conf("dbUser", "ccapi"),
            'PASSWORD': _get_conf("dbPW", ""),
            'NAME': _get_conf("dbName", "ccapi")
        }
    }
else:
    raise RuntimeError("Unknown db_type " +
                       repr(_get_conf("dbType")) + " in config file.")

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static_gen")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]