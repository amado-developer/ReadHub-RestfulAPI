from django.db import models

'''

name varchar 50
author varchar 50
publisher varchar 50
edition integer
release_date date
ISBN varchar 25

'''

class Book(models.Model):
    name            = models.CharField( max_length = 50, null = False )
    author          = models.CharField( max_length = 50, null = False )
    publisher       = models.CharField( max_length = 50, null = False )
    isbn            = models.CharField( max_length = 25, null = False )
    edition         = models.PositiveIntegerField( null = False )
    release_date    = models.DateField(auto_now=False)

class Meta:
    verbose_name = 'Book'
    verbose_name_plural = 'Books'

