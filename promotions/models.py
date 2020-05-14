from django.db import models

class Promotion(models.Model):
    description       = models.CharField( max_length = 50, null = False )
    discount          = models.FloatField()
