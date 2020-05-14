from django.db import models

'''

first_name (varchar 50) (null = false)
last_name (varchar 50) (null = false)
age (int) (null = false)
genre (varchar 20) (null = false)
pseudonym (varchar 50) (null = false)
nationality (varchar 50) (null = true)

'''

class Author(models.Model):
    first_name      = models.CharField(max_length=50, null=False)
    last_name       = models.CharField(max_length=50, null=False)
    age             = models.IntegerField(null=True)
    gender          = models.CharField(max_length=20, null=False)
    pseudonym       = models.CharField(max_length=50, null=False)
    nationality     = models.CharField(max_length=50, null=False)

class Meta:
    verbose_name = 'Author'
    verbose_name_plural = 'Authors'

