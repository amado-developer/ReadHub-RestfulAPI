from django.db import models
'''
name (varchar 50)
author (varchar 50)
publisher (varchar 50)
language (varchar 25)
edition (integer)
release_date (date)
price
doi (varchar 25)

'''

class Audio_Book(models.Model):
    name            = models.CharField( max_length = 50, null = False )
    author          = models.CharField( max_length = 50, null = False )
    publisher       = models.CharField( max_length = 50, null = False )
    language       = models.CharField( max_length = 50, null = False )
    edition         = models.PositiveIntegerField( null = False )
    release_date    = models.DateField(auto_now=False)
    doi            = models.CharField( max_length = 25, null = False )
