from django.db import models
'''
type (varchar 25)
user(FK)
book(FK)
message (varchar 250)
date (date)


'''
class Comment(models.Model):
    message = models.CharField(max_length = 250, null = False )
    date = models.DateField(auto_now=True)
    
    book = models.ForeignKey(
        'digital_books.Digital_Book',
        on_delete = models.CASCADE,
        null = True,
        blank = False
    )

    user = models.ForeignKey(
        'users.User',
        on_delete = models.CASCADE,
        null = True,
        blank = False
    )

    
class Meta:
    verbose_name = 'Comment'
    verbose_name_plural = 'Comments'

