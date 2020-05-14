from rest_framework import serializers
from authors.models import Author

'''

first_name (varchar 50) (null = false)
last_name (varchar 50) (null = false)
age (int) (null = false)
genre (varchar 20) (null = false)
pseudonym (varchar 50) (null = false)
nationality (varchar 50) (null = true)

'''
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            'age',
            'genre',
            'pseudonym',
            'nationality'
        )
