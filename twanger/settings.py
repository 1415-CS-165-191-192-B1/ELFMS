"""
This is our project configuration file. This is imported at runtime and the
values are used to run the app. I will document the items below the best I can.
This is an almost default version of the file and includes everything you need
to get started.
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Random key used to salt the crypto routines and session encryption.
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '57_=o-j*fq=)bsy_(&i#-2d21t5m)(79(pc)6fny2a5mm%u$n0'


# This puts the application in debug mode. You will get fancy error pages with
# stacktraces
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Provides extra debug output on template errors
TEMPLATE_DEBUG = True

# A list of hosts that are allowed to access the app. This is REQUIRED if you
# dont have DEBUG = True.
ALLOWED_HOSTS = []

# A tuple of all the Django applications we are going to use.
INSTALLED_APPS = (
    # These are apps that are built into django:

    # The admin interface
    'django.contrib.admin',
    # The authentication backend that provides the User model
    'django.contrib.auth',
    # The contenttypes framework. Allows arbitrary linking of models.
    'django.contrib.contenttypes',
    # The session framework does all the session handling for you
    'django.contrib.sessions',
    # A messaging app used by the admin interface.
    'django.contrib.messages',
    # An app that helps serve static files on a configurable path.
    'django.contrib.staticfiles',

    # Here are the apps that we have written:

    # The site app holds the homepage and auth stuff. Basically stuff that
    # don't fit anywhere else or are generic.
    'twanger.site',
    # The app that allows posting messages in twanger.
    'twanger.message',
)


# The `middleware` classes are modules that ALL requests are sent through
# before you execute the view. These manipulate the request providing
# more functionality for the view to use.
MIDDLEWARE_CLASSES = (
    # Handles all the session stuff in the request.
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Handles url rewriting and auto `/` additions to the ends of urls.
    'django.middleware.common.CommonMiddleware',
    # Provides per request helpers to protect from Cross-Site Forgery Requests.
    'django.middleware.csrf.CsrfViewMiddleware',
    # Middleware for utilizing Web-server-provided authentication.
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # Stores temporary messages. Mostly used by the admin interface.
    'django.contrib.messages.middleware.MessageMiddleware',
    # Provides click-jacking protection to requests.
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# The root urlconf is where you define the base urls of the entire application.
# From here you can include other urlconfs from applications.
ROOT_URLCONF = 'twanger.urls'

# A auto generated file like manage.py that provides a WSGI interface to your
# project.
WSGI_APPLICATION = 'twanger.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# Here we are using the most basic database type. SQLite is a limited version
# of the SQL database standard that stores it's data in a simple file.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
# These enable and configure the various internationalization modules provided
# by Django.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# This is the url where all your static media files will be served from.
STATIC_URL = '/static/'
