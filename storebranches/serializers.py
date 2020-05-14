
from rest_framework import serializers
from storebranches.models import StoreBrach

class StoreBrachSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreBrach
        fields = (
            'id',
            'location',
            'employee_quantity',
            'phone_number',
            'schedule'
        )