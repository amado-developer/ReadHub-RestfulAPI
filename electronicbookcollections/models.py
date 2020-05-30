from django.db import models

class ElectronicBookCollection(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE, default=None)
    digital_books = models.ForeignKey(to='digital_books.Digital_Book', on_delete=models.CASCADE, default=None)
    
class Meta:
    verbose_name = 'Electronic Book'
    verbose_name_plural = 'Electronic Books'
