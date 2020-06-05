from django.shortcuts import render
from magazines.serializers import MagazinesSerializer
from rest_framework import viewsets
from magazines.models import Magazine
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email
    
class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazinesSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': is_admin,
                    'list': True,
                },
                'instance': {
                    'retrieve': is_logged,
                    'destroy': False,
                    'update': False,
                    'search': is_logged,
                }
            }
        ),
    )

    @action(detail=False ,methods=['get'])
    def search(self, request):
        search_filter = request.query_params['magazineName']
        magazines = Magazine.objects.filter(name__contains= search_filter)
        magazines_response = MagazinesSerializer(magazines, many = True).data
        return Response(magazines_response)
        
