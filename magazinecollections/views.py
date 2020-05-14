from django.shortcuts import render
from rest_framework import viewsets
from .models import MagazineCollection
from .serializer import MagazineCollectionSerializer

class MagazineCollectionViewset(viewsets.ModelViewSet):
    queryset = MagazineCollection.objects.all()
    serializer_class = MagazineCollectionSerializer
