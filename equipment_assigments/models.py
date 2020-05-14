from django.db import models

'''
Equipment_Assigment
id_user (FK)
id_equipment (FK)

'''

class Equipment_Assigment(models.Model):
    '''
    id_user = models.ForeignKey(
        'Users.User',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
'''
    id_equipment = models.ForeignKey(
        'equipments.Equipment',
        on_delete = models.CASCADE,
        null = False,
        blank = False
    )
    
    

    

