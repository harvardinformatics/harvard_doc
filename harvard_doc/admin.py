from django.contrib import admin
from harvard_doc.models import Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'user',)
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Document, DocumentAdmin)
