from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = (
            'id',
            'for_sale',
            'price',
            'digital_book'
        )