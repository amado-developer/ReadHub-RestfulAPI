from django.db import models

class Collection(models.Model):
    description = models.CharField(max_length=50, null=False )

class Meta:
    verbose_name = 'Collection'
    verbose_name_plural = 'Collections'
