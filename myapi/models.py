from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Car(models.Model):
    name = models.CharField(blank=False, max_length=60)
    year = models.IntegerField(blank=False, max_length=4, help_text=_("Release year"))

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("Cars")