from django.contrib import admin
from billing_record.models import BillingRecord

class BillingRecordAdmin(admin.ModelAdmin):
    list_display = ('name', 'payment_code', 'amount', 'bill_date',)
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(BillingRecord, BillingRecordAdmin)
