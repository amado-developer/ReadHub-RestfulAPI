from django.shortcuts import render
from rest_framework import viewsets
from .models import Collection
from .serializers import CollectionSerializer

class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects().all()
    serializer_class = CollectionSerializer
