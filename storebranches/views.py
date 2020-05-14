from rest_framework import viewsets
from django.shortcuts import render
from storebranches.models import StoreBrach
from storebranches.serializers import StoreBrachSerializer


class StoreBrachViewSet(viewsets.ModelViewSet):
    queryset = StoreBrach.objects.all()
    serializer_class = StoreBrachSerializer
