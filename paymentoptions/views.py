from django.shortcuts import render
from paymentoptions.models import PaymentOption
from paymentoptions.serializers import  PaymentOptionSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from users.models import User

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email
    
class PaymentOptionViewSet(viewsets.ModelViewSet):
    queryset = PaymentOption.objects.all()
    serializer_class = PaymentOptionSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': is_admin,
                    'list': True,
                },
                'instance': {
                    'retrieve': is_logged,
                    'destroy': False,
                    'update': False,
                    'change_payment_option': is_logged,
                    'get_payment_option': is_logged,
                }
            }
        ),
    )
    @action(detail=False, url_path='change-payment-option', methods=['post', 'patch'])
    def change_payment_option(self, request):
        card_holder = request.data['cardHolder']
        card_number = request.data['cardNumber']
        exp_date = request.data['expDate']
        cvv = request.data['cvv']

        if request.method == 'POST':
            user_id = request.query_params['user']
            user = User.objects.get(pk=user_id)
            pay = PaymentOption()
            pay.user = user
            pay.card_holder = card_holder
            pay.card_number = card_number
            pay.exp_date = exp_date
            pay.cvv = cvv
            pay.save()
            return Response({"Succesfully Added: Payment option"})
        else:
            try:
                user_id= request.query_params['user']
                user = User.objects.get(pk=user_id)
                pay = PaymentOption.objects.get(user=user)
                pay.card_holder = card_holder
                pay.card_number = card_number
                pay.exp_date = exp_date
                pay.cvv = cvv
                pay.save()

            except User.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        return Response({})
    
    @action(detail=False, url_path='get-payment-option', methods=['get'])
    def get_payment_option(self, request):
        user_id = request.query_params['user']
        user = User.objects.get(pk=user_id)
        pay = PaymentOption.objects.filter(user=user).values()
    
        return Response(pay)


        




    