from django.shortcuts import render
from rest_framework import viewsets
from .models import ElectronicBookCollection
from .serializer import ElectronicBookCollectionSerializer

class ElectronicBookCollectionViewset(viewsets.ModelViewSet):
    queryset = ElectronicBookCollection.objects.all()
    serializer_class = ElectronicBookCollectionSerializer
