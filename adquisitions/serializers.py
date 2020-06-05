from rest_framework import serializers
from .models import Collection
from rest_framework.validators import UniqueTogetherValidator
class CollectionSerializer(serializers.ModelSerializer):
    book = serializers.SerializerMethodField()
    class Meta:
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Collection.objects.all(),
        #         fields=['user', 'book']
        #     )
        # ]
        model = Collection
        fields = (
            'id',
            'user',
            'book',
            'description',
        )
    def get_book(self, obj):
        return { 
            "id": obj.book.id,
            "name": obj.book.name,
            "author": obj.book.author.pseudonym,
            "publisher": obj.book.publisher,
            "edition": obj.book.edition,
            "release_date": obj.book.release_date,
            "doi": obj.book.doi,
            "cover": obj.book.cover.url,
            }

    