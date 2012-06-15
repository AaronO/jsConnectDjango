# Django imports
from django.conf.urls import patterns, url

# Local imports
from .views import js_connect_auth_view

# Our URLPatterns
urlpatterns = patterns('',
    url(r'^$', js_connect_auth_view,name = 'js_connect_index'),
)
