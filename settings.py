# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *

import os

#### {
#from ragendja.settings_pre import * # do we need ragendja
# import unsaved_settings # do we need this? how can we get it?

MEDIA_VERSION = 1
DJANGO_STYLE_MODEL_KIND = False
TIME_ZONE = 'GMT'
COMBINE_MEDIA = {
  'combined-%(LANGUAGE_CODE)s.js': (
    '.site_data.js',
  ),
  'combined-%(LANGUAGE_DIR)s.css': (
    'global/look.css',
  ),
}
ADMINS = (('childhealth Administrators', 'childhealth-admin@maventy.org'),)
EMAIL_SUBJECT_PREFIX = '[childhealth] '
EMAIL_SIGNATURE = 'Maventy.org child health system'
SEND_BROKEN_LINK_EMAILS = True

if on_production_server:
  DEFAULT_FROM_EMAIL = 'dan@maventy.org'
  SERVER_EMAIL = DEFAULT_FROM_EMAIL
  TEMPLATE_STRING_IF_INVALID = ""
else:
  TEMPLATE_STRING_IF_INVALID = "[[ UNDEFINED VARIABLE ]]"

FILE_UPLOAD_MAX_MEMORY_SIZE = 1048576  # 1 MB

gettext = lambda s: s
LANGUAGES = (
  ('en', 'English'),
  ('fr', 'Francaise'),
)
#### }

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    #### {
    'django.contrib.webdesign',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.sites',
    # 'appenginepatcher',
    # 'ragendja',
    'healthdb',
    'registration',
    'search',
    #### }

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #### {
    # 'ragendja.middleware.ErrorMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    #### }
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    #### {
    'django.core.context_processors.i18n',
    'healthdb.context_processors.vars',
    #### }
)

#### {
AUTH_USER_MODULE = 'healthdb.custom_user_model'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'
#### }

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

STATIC_URL = '/static/'

TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'

#### {
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
  'healthdb',
)
DATABASE_OPTIONS = {
  'remote_url': '/remote-api-34358334',
}
#from ragendja.settings_post import *
RECAPTCHA_PUBLIC_KEY = '6Le8qwgAAAAAAFTckJQI1ucaGJ_DDfuY4XUgJotb'
# RECAPTCHA_PRIVATE_KEY = unsaved_settings.RECAPTCHA_PRIVATE_KEY

########## CHANGE THIS!!!! ############# CHANGE THIS!!! ##############
RECAPTCHA_PRIVATE_KEY = '6Le8qwgAAAAAAFTckJQI1ucaGJ_DDfuY4XUgJotb'
######################################################################

#### {