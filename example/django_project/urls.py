from django.conf.urls import patterns, include, url

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin
    url(r'^admin/', include(admin.site.urls)),

    # jsConnect 
    url(r'jsconnect/', include('jsConnectDjango.urls')),
)
