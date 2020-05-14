from django.shortcuts import render
from rest_framework import permissions
from rest_framework import viewsets



from users.serializers import RegistrationSerializer
from .models import User

class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    permission_classes = [
        permissions.AllowAny 
    ]
  