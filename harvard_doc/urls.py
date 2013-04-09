from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('harvard_doc.views',
   #web
   url(r'^$', 'html_view'),
   url(r'^html/$', 'html_view'),
   #pdf
   url(r'^pdf/$', 'pdf_view'),

)
