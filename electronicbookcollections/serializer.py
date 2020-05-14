from rest_framework import serializers
from .models import ElectronicBookCollection

class ElectronicBookCollectionSerializer(serializers.ModelSerializer):
    model = ElectronicBookCollection
    fields = (
        'id',
        'collection_id'
    )