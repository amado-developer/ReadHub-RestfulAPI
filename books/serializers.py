from rest_framework import serializers
from books.models import Book

'''

name (varchar 50) (null = false)
author (FK) 
publisher (varchar 50) (null = true)
language (varchar 25)
edition (integer) (null = true)
release_date (date) (null = true)
isbn (varchar 25) (null = false)
for_sale true (null = false)
price (float)
quantity 10 (null = true)


'''
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'name',
            'author',
            'publisher',
            'edition',
            'release_date',
            'isbn',
            'quantity',
            'cover',
        )
        