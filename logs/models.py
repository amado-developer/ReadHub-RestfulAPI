from django.db import models

'''

activity
datetime
user (FK)
type


'''
class Log(models.Model):
    activity    = models.CharField(max_length=50, null=False, default='')
    datetime    = models.DateTimeField(auto_now=True)
    user        = models.ForeignKey(
        to='users.User'
        ,on_delete=models.CASCADE
    )

class Meta:
    verbose_name = 'Log'
    verbose_name_plural = 'Logs'
