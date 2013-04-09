from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from django.contrib.auth.models import User
from harvard_doc.models import Document
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization

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
