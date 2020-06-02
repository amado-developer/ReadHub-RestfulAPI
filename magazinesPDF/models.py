from django.db import models

class MagazinesPDF(models.Model):
    magazine = models.ForeignKey(to='magazines.Magazine', on_delete=models.CASCADE, default=0)
    pdf = models.FileField(null=False)


class Meta:
    verbose_name = 'Magazine PDF'
    verbose_name_plural= 'Magazines PDF'
