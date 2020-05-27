from django.db import models

class Inventory(models.Model):
    for_sale = models.BooleanField(default=True)
    price    = models.FloatField(null=False)
    digital_book     = models.ForeignKey(
        to='digital_books.digital_book', on_delete=models.CASCADE, default=0
    )

class Meta:
    verbose_name = 'Inventory'
    verbose_name_plural = 'Inventories'
