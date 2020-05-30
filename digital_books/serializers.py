from rest_framework import serializers
from digital_books.models import Digital_Book

class digital_bookSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    class Meta:
        model = Digital_Book
        fields = (
            'id',
            'name',
            'author',
            'language',
            'publisher',
            'edition',
            'release_date',
            'price',
            'doi',
            'cover',
        )

    def get_author(self, obj):
        return obj.author.pseudonym