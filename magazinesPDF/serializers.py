from .models import MagazinesPDF
from rest_framework import serializers

class MagazinePDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = MagazinesPDF
        fields= (
            'id',
            'magazine',
            'pdf'
        )

