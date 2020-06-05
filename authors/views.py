from django.shortcuts import render
from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': is_admin,
                    'list': True,
                },
                'instance': {
                    'retrieve': is_admin,
                    'destroy': is_admin,
                    'update': is_admin,
                }
            }
        ),
    )