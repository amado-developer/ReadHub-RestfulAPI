from django.db import models

class MagazineCollection(models.Model):
    collection_id = models.ForeignKey(
        to='adquisitions.Collection',
        on_delete=models.CASCADE
    )
class Meta:
    verbose_name = 'Magazine Collection'
    verbose_name_plural = 'Magazine Collections'
