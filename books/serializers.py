from rest_framework import serializers
from books.models import Book

'''

name varchar 50
author varchar 50
publisher varchar 50
edition integer
release_date date
ISBN varchar 25

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
        )
        