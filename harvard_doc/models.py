from django.db import models
from datetime import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import User

class Document(models.Model):
    name = models.CharField(max_length=100, default="", null=False)
    url = models.URLField(max_length=300, default="", null=False, blank=False)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, null=False, default=datetime.utcnow().replace(tzinfo=utc))
    modified = models.DateTimeField(auto_now=True, null=False, default=datetime.utcnow().replace(tzinfo=utc))

    def __unicode__(self):
        return self.name
        
    def generate_pdf(self):
        return self.url
