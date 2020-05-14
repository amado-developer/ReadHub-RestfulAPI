from django.shortcuts import render
from rest_framework import viewsets
from equipments.models import Equipment
from  equipments.serializers import EquipmentSerializer


class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer

