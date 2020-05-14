from rest_framework import serializers
from equipments.models import Equipment

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = (
            'id',
            'name', 
            'type',
            'transaction_date',
            'quantity'
        )
