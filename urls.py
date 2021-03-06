from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
#from admin_apps.settings import local as settings
from tastypie.api import Api
from api import DocumentResource, UserResource

admin.autodiscover()

api = Api(api_name='api')
api.register(UserResource())
api.register(DocumentResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dokken.views.home', name='home'),
    # url(r'^dokken/', include('dokken.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^harvard_doc/', include('harvard_doc.urls')),
    (r'^a/', include(api.urls)),
)
