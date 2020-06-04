from django.shortcuts import render
from rest_framework import viewsets
from equipments.models import Equipment
from  equipments.serializers import EquipmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

    @action(detail=False ,methods=['get'])
    def search(self, request):
        search_filter = request.query_params['equipmentName']
        equipments = Equipment.objects.filter(name__contains= search_filter)
        equipments_response = EquipmentSerializer(equipments, many = True).data
        return Response(equipments_response)

