from django.db import models

'''
name (varchar 50) (null = false)
author (FK) 
publisher (varchar 50) (null = true)
language (varchar 25)
edition (integer) (null = true)
release_date (date) (null = true)
isbn (varchar 25) (null = false)
for_sale true (null = false)
price (float)
quantity 10 (null = true)

'''

class Book(models.Model):
    name            = models.CharField( max_length=50, null=False )
    author          = models.ForeignKey(to='authors.Author', on_delete=models.CASCADE)
    publisher       = models.CharField( max_length=50, null=False )
    language        = models.CharField( max_length=50, null=False, default='English')
    isbn            = models.CharField( max_length=25, null=False )
    edition         = models.PositiveIntegerField(null=False )
    release_date    = models.DateField(auto_now=False, null=False)
    quantity        = models.PositiveIntegerField(default=0)
    cover           = models.ImageField(null=False, default='')

class Meta:
    verbose_name = 'Book'
    verbose_name_plural = 'Books'

