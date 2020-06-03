from django.db import models

class EquipmentLoan(models.Model):
     user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
     equipment = models.ForeignKey(to='equipments.Equipment', on_delete=models.CASCADE)
     loan_date = models.DateField(auto_now=True)
     devolution_date = models.DateField(auto_now=False)
     fee = models.FloatField(null=True)

class Meta:
    verbose_name = 'Equipment Loan'
    verbose_name_plural = 'Equipment Loans'
