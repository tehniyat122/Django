from django.db import models
from django.utils import timezone

# Create your models here.
class tehnia(models.Model):
    name = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    created = models.DateTimeField('date_created', default=timezone.now(), blank=False)
    def __unicode__(self):
        return self.name
