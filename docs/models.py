from django.db import models
from datetime import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import User
#from payment_type.models import PaymentType

# Create your models here.

class Document(models.Model):
    #logo_path = os.path.join(STATIC_ROOT, 'logos')
    name = models.CharField(max_length=100, default="", null=False)
    #payment_type = models.ForeignKey(PaymentType)
    content = models.CharField(max_length=10000, default="", null=False)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, null=False, default=datetime.utcnow().replace(tzinfo=utc))
    modified = models.DateTimeField(auto_now=True, null=False, default=datetime.utcnow().replace(tzinfo=utc))

    def __unicode__(self):
        return self.name
