from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', '{{ app|lower }}.views.home', name='home'),
    # url(r'^{{ app|lower }}/', include('{{ app|lower }}.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
