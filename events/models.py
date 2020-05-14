from django.db import models

'''

description
type
datetime

'''

class Event(models.Model):
    type        = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=50, null=False)
    datetime    = models.DateTimeField()

class Meta:
    verbose_name = 'Event'
    verbose_name_plural = 'Events'
