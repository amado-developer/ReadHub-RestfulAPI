from django.db import models

class StudyClassrooms_Reservation(models.Model):
    user = models.ForeignKey(to='users.User', on_delete=models.CASCADE)
    study_classroom = models.ForeignKey('studyclassrooms.StudyClassrooom',on_delete = models.CASCADE, null = False,blank = False)
    loan_date = models.DateField(auto_now=True)
    devolution_date = models.DateField(auto_now=False)
    
  

    


