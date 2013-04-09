from tastypie.resources import ModelResource
from tastypie.constants import ALL, ALL_WITH_RELATIONS
from django.contrib.auth.models import User
from billing_record.models import BillingRecord
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization, Authorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'

class BillingRecordResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = BillingRecord.objects.all()
        limit = 0
        filtering = {
            'payment_code': ('exact', 'endswith'),
            'bill_date': ('gte', 'lt'),
            }
        authentication = BasicAuthentication()
        #authorization= Authorization()
        authorization = DjangoAuthorization()
