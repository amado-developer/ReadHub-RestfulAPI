from paymentoptions.models import PaymentOption
from rest_framework import serializers
from paymentoptions.models import PaymentOption

class PaymentOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOption
        fields = (
            'id',
            'user,'
            'card_holder',
            'card_number',
            'exp_date'
            'cvv',
        )

        extra_kwargs = {
            'cvv' :{'write_only' : True },
        }