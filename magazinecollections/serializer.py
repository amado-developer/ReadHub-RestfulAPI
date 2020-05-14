from rest_framework import serializers
from .models import MagazineCollection

class MagazineCollectionSerializer(serializers.ModelSerializer):
    model = MagazineCollection
    fields = (
        'id',
        'collection_id'
    )