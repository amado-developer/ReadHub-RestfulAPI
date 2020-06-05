from django.shortcuts import render
from rest_framework import viewsets
from equipments.models import Equipment
from  equipments.serializers import EquipmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

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
                    'search': is_logged,
                }
            }
        ),
    )

    @action(detail=False ,methods=['get'])
    def search(self, request):
        search_filter = request.query_params['equipmentName']
        equipments = Equipment.objects.filter(name__contains= search_filter)
        equipments_response = EquipmentSerializer(equipments, many = True).data
        return Response(equipments_response)


