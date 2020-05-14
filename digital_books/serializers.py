from rest_framework import serializers
from digital_books.models import digital_book

class digital_bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = digital_book
        fields = (
            'id',
            'name',
            'author',
            'language',
            'publisher ',
            'edition ',
            'release_date ',
            'price ',
            'doi ',
        )