"""
Django CI settings for ELFMS project.
"""
from .settings import * # import common settings

# Application definition
INSTALLED_APPS += (
    'django_jenkins',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'elfms',
        'USER': 'marashen',
        'PASSWORD': '123',
        'HOST': 'localhost',
    }
}

JENKINS_TASKS = (
    'django_jenkins.tasks.run_jshint',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount',
)

PYLINT_RCFILE = 'pylint.rc'
