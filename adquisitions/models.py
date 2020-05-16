from django.db import models

class Collection(models.Model):
    user         = models.ForeignKey(
        to='users.User', on_delete=models.CASCADE, default=0
    )

    book         = models.ForeignKey(
        to='books.Book', on_delete=models.CASCADE, default=0,
    )
    description  = models.CharField(max_length=50, null=True )

class Meta:
    verbose_name = 'Collection'
    verbose_name_plural = 'Collections'
