from django.shortcuts import render
from magazines.serializers import MagazinesSerializer
from rest_framework import viewsets
from magazines.models import Magazine
# Create your views here.

class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazinesSerializer
