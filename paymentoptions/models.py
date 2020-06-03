from django.db import models

class PaymentOption(models.Model):
    user            = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    card_holder     = models.CharField(max_length=50, null=False)
    card_number     = models.CharField(max_length=50, null=False)
    exp_date        = models.CharField(max_length=50, null=False)
    cvv             = models.CharField(max_length=50, null=False, default=0)

class Meta:
    verbose_name = 'Payment Option'
    verbose_name_plural = 'Payment Options'
