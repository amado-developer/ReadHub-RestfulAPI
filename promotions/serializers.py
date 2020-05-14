from rest_framework import serializers
from promotions.models import Promotion

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        field = (
            'id',
            'description',
            'discount'
        )