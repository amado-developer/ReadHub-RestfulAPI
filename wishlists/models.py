from django.db import models

'''
user (FK)
book (FK)

'''
class WishList(models.Model):
    user = models.ForeignKey(
        to='users.User',
        on_delete=models.CASCADE
    )

    book = models.ForeignKey(
        to='books.Book',
        on_delete=models.CASCADE
    )

    '''
    electronic_book = models.ForeignKey(
        to='electronicbooks.ElectronicBook', 
        on_delete=models.CASCADE
    )
    '''

    '''
    magazine = models.ForeignKey(
        to='magazines.Magazine', 
        on_delete=models.CASCADE

    '''
