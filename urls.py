from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    #(r'^demojuan/', include('demojuan.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^', include('demojuan.apps.home.urls')),
     url(r'^', include('demojuan.apps.webServices.wsProductos.urls')),
    # Uncomment the next line to enable the admin:
     #(r'^admin/', include(admin.site.urls)),
     (r'^admin/(.*)', admin.site.root),

)
