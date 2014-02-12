from ragendja.settings_pre import *
import unsaved_settings

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
  ('fr', 'Française'),
)
TEMPLATE_CONTEXT_PROCESSORS = (
  'django.core.context_processors.auth',
  'django.core.context_processors.media',
  'django.core.context_processors.request',
  'django.core.context_processors.i18n',
  'healthdb.context_processors.vars',
)
MIDDLEWARE_CLASSES = (
  'ragendja.middleware.ErrorMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.middleware.common.CommonMiddleware',
  'ragendja.sites.dynamicsite.DynamicSiteIDMiddleware',
  'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
  'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
)
AUTH_USER_MODULE = 'healthdb.custom_user_model'
LOGIN_URL = '/account/login/'
LOGOUT_URL = '/account/logout/'
LOGIN_REDIRECT_URL = '/'

INSTALLED_APPS = (
  'django.contrib.auth',
  'django.contrib.sessions',
  'django.contrib.admin',
  'django.contrib.webdesign',
  'django.contrib.flatpages',
  'django.contrib.redirects',
  'django.contrib.sites',
  'appenginepatcher',
  'ragendja',
  'healthdb',
  'registration',
  'search',
)
IGNORE_APP_SETTINGS = IGNORE_APP_URLSAUTO = (
  'healthdb',
)
DATABASE_OPTIONS = {
  'remote_url': '/remote-api-34358334',
}
from ragendja.settings_post import *
RECAPTCHA_PUBLIC_KEY = '6Le8qwgAAAAAAFTckJQI1ucaGJ_DDfuY4XUgJotb'
RECAPTCHA_PRIVATE_KEY = unsaved_settings.RECAPTCHA_PRIVATE_KEY