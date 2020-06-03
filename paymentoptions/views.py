from django.shortcuts import render
from paymentoptions.models import PaymentOption
from paymentoptions.serializers import  PaymentOptionSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import User


class PaymentOptionViewSet(viewsets.ModelViewSet):
    queryset = PaymentOption.objects.all()
    serializer_class = PaymentOptionSerializer


    @action(detail=False, url_path='change-payment-option', methods=['patch'])
    def change_paymentOption(self, request):
        user_id= request.query_params['user']
        user = User.objects.get(pk=user_id)
        try:
            pay = PaymentOption.objects.get(pk=user)
            pay.save()

        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)





    