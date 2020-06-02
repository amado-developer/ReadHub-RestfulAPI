from rest_framework import serializers
from .models import DigitalBookPDF

class DigitalBookPDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalBookPDF
        fields = (
            'id',
            'book',
            'pdf',
        )