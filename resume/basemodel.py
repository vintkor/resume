from django.db import models
from django.utils.translation import ugettext as _


class AbstractDateModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name=_('Updated'))

    class Meta:
        abstract = True

    objects = models.Manager()
