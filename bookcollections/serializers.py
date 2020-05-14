from rest_framework import serializers
from .models import BookCollection

class BookCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        module = BookCollection
        fields = (
            'id',
            'collection_id',
        )
    