from django.db import models
'''
type (varchar 25)
user(FK)
book(FK)
message (varchar 250)
date (date)


'''
class Comment(models.Model):
    type = models.CharField(max_length = 50, null = False )
    message = models.CharField(max_length = 250, null = False )
    date = models.DateField(auto_now=False)
    
    book = models.ForeignKey(
        'books.Book',
        on_delete = models.CASCADE,
        null = True,
        blank = False
    )
    '''
    user = models.ForeignKey(
        'Users.User',
        on_delete = models.CASCADE,
        null = True,
        blank = False
    )
    '''
    
class Meta:
    verbose_name = 'Comment'
    verbose_name_plural = 'Comments'

