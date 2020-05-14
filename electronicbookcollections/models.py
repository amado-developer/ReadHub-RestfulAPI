from django.db import models

class ElectronicBookCollection(models.Model):
    collection_id = models.CharField(max_length=50, null=False)

class Meta:
    verbose_name = 'Electronic Book'
    verbose_name_plural = 'Electronic Books'
