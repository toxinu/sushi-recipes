import dj_database_url

from {{ app|lower }}.settings.common import *

#==============================================================================
# Generic Django project settings
#==============================================================================

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': dj_database_url.config()
}
