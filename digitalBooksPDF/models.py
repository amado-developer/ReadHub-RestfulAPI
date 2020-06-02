from django.db import models


class DigitalBookPDF(models.Model):
    book = models.ForeignKey(to='digital_books.Digital_Book', on_delete=models.CASCADE, default=0)
    pdf = models.FileField(null=False)

class Meta:
    verbose_name = 'Digital Book PDF'
    verbose_name_plural= 'Digital Books PDF'

