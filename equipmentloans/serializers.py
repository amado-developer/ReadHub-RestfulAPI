from equipmentloans.models import EquipmentLoan
from rest_framework import serializers
from equipmentloans.models import EquipmentLoan


class EquipmentLoanSerializer(serializers.ModelSerializer):
    equipment = serializers.SerializerMethodField()
    class Meta:
        model = EquipmentLoan
        fields = (
            'id',
            'user',
            'equipment',
            'loan_date',
            'devolution_date',
            'fee'
        )
    def get_equipment(self, object):
        return {
            "id" : object.equipment.id,
            "name": object.equipment.name,
            "type": object.equipment.type,
            "quantity": object.equipment.quantity
        }