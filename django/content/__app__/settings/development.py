import os

from {{ app|lower }}.settings.common import *

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'dev.sqlite3',
    }
}
