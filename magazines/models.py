from django.db import models

'''
name (varchar 50)
author (varchar 50)
volume(int 10)
release_date (date)
number (int 10)
quantity (int)
'''

class Magazine(models.Model):
    name            = models.CharField( max_length = 50, null = False )
    author          = models.CharField( max_length = 50, null = False )
    volume          = models.CharField( max_length = 50, null = False )
    release_date    = models.DateField(auto_now=False)
    number          = models.CharField( max_length = 25, null = False )
    cover = models.ImageField(null=False, default='')
    price = models.DecimalField(decimal_places=2, max_digits=6, default=0.0 )

class Meta:
    verbose_name = 'Magazine'
    verbose_name_plural = 'Magazines'