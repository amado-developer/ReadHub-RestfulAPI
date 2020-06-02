from rest_framework import serializers
from .models import MagazineCollection
from rest_framework.validators import UniqueTogetherValidator

class MagazineCollectionSerializer(serializers.ModelSerializer):
    magazine = serializers.SerializerMethodField()
    class Meta:
        model = MagazineCollection
        fields = (
            'id',
            'user',
            'magazine',
            'description'
    )
    
    def get_magazine(self, obj):
        return{
            "id": obj.magazine.id,
            "name": obj.magazine.name,
            "author": obj.magazine.author,
            "volume": obj.magazine.volume,
            "release_date": obj.magazine.release_date,
            "number": obj.magazine.number,
            "cover": obj.magazine.cover.url,
            "price": obj.magazine.price,

        }
        

