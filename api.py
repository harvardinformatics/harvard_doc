from django.conf.urls.defaults import *
from django.contrib.auth.models import User
from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.utils import trailing_slash
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization
from harvard_doc.models import Document
from harvard_doc.views import pdf_view, html_view

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class DocumentResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Document.objects.all()
        limit = 0
        filtering = {
            'name': ('exact', 'startswith'),
            'created': ('gte', 'lt'),
            }
        authentication = BasicAuthentication()
        #authorization= Authorization()
        authorization = DjangoAuthorization()
