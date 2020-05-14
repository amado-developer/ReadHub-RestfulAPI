from django.db import models

class BookCollection(models.Model):
    collection_id = models.ForeignKey(
        to='adquisitions.Collection'
        , on_delete=models.CASCADE
        )
class Meta:
    verbose_name = 'Book Collection'
    verbose_name_plural = 'Book Collections'
