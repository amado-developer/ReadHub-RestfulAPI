from rest_framework import serializers
from magazines.models import Magazine

class MagazinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Magazine
        fields = (
            'id',
            'name',
            'author',
            'volume',
            'release_day',
            'number',
            'quantity',
        )