from django.db import models

'''
name (varchar 50)
type (varchar 50)
transaction_date (date)
quantity (integer)
'''

class Equipment(models.Model):
    name = models.CharField(max_length = 50, null = False)
    type = models.CharField(max_length = 50, null = False)
    transaction_date = models.DateField(auto_now=False)
    quantity = models.PositiveIntegerField(null = False)

class Meta:
    verbose_name = 'Equipment'
    verbose_name_plural = 'Equipments'

