from rest_framework import serializers
from audio_books.models import Audio_Book


class Audio_BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio_Book
        fields = (
            'id',
            'name',
            'author',
            'publisher',
            'language',
            'edition',
            'release_date',
            'doi',
        )
