from django.db import models

class MagazineCollection(models.Model):
    user= models.ForeignKey(to='users.User', on_delete=models.CASCADE, default=0)
    magazine= models.ForeignKey(to='magazines.Magazine', on_delete=models.CASCADE, default=0,)
    description  = models.CharField(max_length=50, null=True )

class Meta:
    verbose_name = 'Magazine Collection'
    verbose_name_plural = 'Magazine Collections'
