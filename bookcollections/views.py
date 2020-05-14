from django.shortcuts import render
from rest_framework import viewsets
from .models import BookCollection
from .serializers import BookCollectionSerializer

class BookCollectionViewset(viewsets.ModelViewSet):
    queryset = BookCollection.objects.all()
    serializer_class = BookCollectionSerializer
