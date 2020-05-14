from django.db import models
'''
User
study classroom (FK)
enter_hour (datetime) 
return_hour (datetime) 

'''
class StudyClassrooms_Reservation(models.Model):
    user            = models.CharField( max_length = 50, null = False )
    enter_hour      = models.DateField(auto_now=False)
    return_hour     = models.DateField(auto_now=False)

    study_classroom = models.ForeignKey(
        'studyclassrooms.StudyClassrooom',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
  

    


