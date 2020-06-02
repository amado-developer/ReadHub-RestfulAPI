from django.db import models

class BookLoan(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    book = models.ForeignKey(to='books.Book', on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now=True)
    devolution_date = models.DateField(auto_now=False)
    fee = models.FloatField(null=True)


class Meta:
    verbose_name = 'Book Loan'
    verbose_name_plural = 'Book Loans'
    
