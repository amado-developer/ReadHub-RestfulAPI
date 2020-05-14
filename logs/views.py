from django.shortcuts import render
from rest_framework import viewsets
from .models import Log
from .serializers import LogSerializer

class LogViewset(viewsets.ModelViewSet):
    queryset = Log.object.all()
    serializer_class = LogSerializer
