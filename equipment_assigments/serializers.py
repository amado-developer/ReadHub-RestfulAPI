from rest_framework import serializers
from equipment_assigments.models import Equipment_Assigment


class Equipment_AssigmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipment_Assigment
        fields = (
            'id',
            'id_user',
            'id_equipment',
        )



    