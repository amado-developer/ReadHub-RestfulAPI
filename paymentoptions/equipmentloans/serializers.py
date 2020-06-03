from equipmentloans.models import EquipmentLoan
from rest_framework import serializers
from equipmentloans.models import EquipmentLoan


class EquipmentLoanSerializer(serializers.ModelSerializer):
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