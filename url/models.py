from django.db import models
import uuid
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Url(models.Model):
    url=        models.URLField(max_length=1000, verbose_name=_("Url:"), help_text=_('Introduce una url para acortar.'))
    shorturl=   models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date=       models.DateField(auto_now_add=True)

class UrlForm(ModelForm):
    class Meta:
        model=Url
        fields = ['url',]
        
