from rest_framework import serializers
from .models import Collection
from rest_framework.validators import UniqueTogetherValidator
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Collection.objects.all(),
        #         fields=['user', 'book']
        #     )
        # ]
        model = Collection
        fields = (
            'id',
            'user',
            'book',
            'description',
        )

    