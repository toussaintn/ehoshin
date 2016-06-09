"""
Django settings for eHoshin project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

############################
# ## Parameter to adapt ## #
############################

# The name of your app used for the authentication
# https://docs.djangoproject.com/fr/1.9/intro/tutorial01/ tuto to create app
AUTHENTICATION_APP = None

# Let the possibility or not to the user to signup
# Set False if the authentication system is external to the website
CAN_SIGNUP = True

# SECURITY WARNING: keep the secret key used in production secret!
# Create you own secret key
SECRET_KEY = None   ### To generate ###

################################
# ## End parameter to adapt ## #
################################

# ## You can modify the settings below but do it carefully ! ## #
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

SECURE_FRAME_DENY = True

## Heroku part, doesn't work...
# DATABASES['default'] =  dj_database_url.config()

TIME_FORMAT = '%H:%M'
DATE_FORMAT = '%d %b'
DATETIME_FORMAT = DATE_FORMAT + ', ' + TIME_FORMAT
DATETIME_INPUT_FORMATS = DATETIME_FORMAT

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'eHoshin',
    'users',
    'teams',
    'hoshins',

    # To let at the bottom
    'notifications',
]

if AUTHENTICATION_APP:
    INSTALLED_APPS.append(AUTHENTICATION_APP)

#############################
# Installed apps parameters #
#############################

# rest_framework app #
######################

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'rest_framework.filters.DjangoFilterBackend',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DATETIME_INPUT_FORMATS': (DATETIME_FORMAT, ),
    'DATETIME_FORMAT': DATETIME_FORMAT,

}

# Notification app #
####################

NOTIFICATIONS_USE_JSONFIELD=True

#################################
# End Installed apps parameters #
#################################



MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'eHoshin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/',
        ],
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

WSGI_APPLICATION = 'eHoshin.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    BASE_DIR + STATIC_URL,
)

STATIC_ROOT = '/'.join([BASE_DIR, "static_production"])

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True