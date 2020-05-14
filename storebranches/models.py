from django.db import models
'''
location (varchar 50)
employee_quantity (int)
phone_number (varchar 50)
schedule (varchar 50)

'''

class StoreBrach(models.Model):
    location                = models.CharField(max_length=50, null = False)
    employee_quantity       = models.PositiveIntegerField(null = False)
    phone_number            = models.CharField(max_length=50, null = False)
    schedule                = models.CharField(max_length=50, null = False)
'''
class Meta:
    verbose_name = 'Store Brach'
    verbose_name_plural = 'Store Braches'
  '''  
