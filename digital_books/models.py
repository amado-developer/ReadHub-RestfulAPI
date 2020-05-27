from django.db import models

'''
name (varchar 50)
author (varchar 50)
language (varchar 25)
publisher (varchar 50)
edition (integer)
release_date (date)
price 
doi (varchar 25)

'''

class digital_book(models.Model):
    name = models.CharField(max_length=50, null=False)
    author = models.CharField(max_length=50, null=False)
    language = models.CharField(max_length=50, null=False)
    publisher = models.CharField(max_length=50, null=False)
    edition =  models.PositiveIntegerField()
    release_date = models.DateField(auto_now=False)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    doi = models.CharField(max_length=50, null=False)
    cover = models.ImageField(null=False, default='')


