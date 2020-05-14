from django.shortcuts import render
from rest_framework import viewsets
from equipment_assigments.models import Equipment_Assigment
from equipment_assigments.serializers import Equipment_AssigmentSerializer

class Equipment_AssigmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment_Assigment.objects.all()
    serializer_class = Equipment_AssigmentSerializer
