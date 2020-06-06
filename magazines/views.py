from django.shortcuts import render
from magazines.serializers import MagazinesSerializer
from rest_framework import viewsets
from magazines.models import Magazine
from magazinecollections.models import MagazineCollection
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
        user = request.query_params['user']
        print('el name')
        print(search_filter)
        magazines = Magazine.objects.filter(name__contains= search_filter)
        users_current_magazines = MagazineCollection.objects.filter(user=user).values()
        magazine_list = list(magazines)
        collection = list(users_current_magazines)
        filtered_magazines_list = []
        for magazine in magazine_list:
            for m in collection:
                if m['magazine_id'] == magazine.id:
                    filtered_magazines_list.append(magazine)

        for magazine in filtered_magazines_list:
            magazine_list.remove(magazine)
  

        magazines_response = MagazinesSerializer(magazine_list, many = True).data
        return Response(magazines_response)
        
