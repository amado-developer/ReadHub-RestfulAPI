from django.db import models

class Inventory(models.Model):
    for_sale = models.BooleanField(default=True)
    price    = models.FloatField(null=False)
    book     = models.ForeignKey(
        to='books.Book', on_delete=models.CASCADE
    )

class Meta:
    verbose_name = 'Inventory'
    verbose_name_plural = 'Inventories'
