from django.db import models
'''
number (varchar 50)
'''

class StudyClassrooom(models.Model):
    number        = models.CharField(max_length=50, null=False)
    
