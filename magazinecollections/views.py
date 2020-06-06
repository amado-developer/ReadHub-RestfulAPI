from django.shortcuts import render
from rest_framework import viewsets
from .models import MagazineCollection
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from users.models import User
from users.serializers import UserSerializer
from magazinecollections.models import MagazineCollection
from magazinecollections.serializers import MagazineCollectionSerializer
from magazines.models import Magazine
from magazines.serializers import MagazinesSerializer

from django.http.response import JsonResponse
import json

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email

class MagazineCollectionViewset(viewsets.ModelViewSet):
    queryset = MagazineCollection.objects.all()
    serializer_class = MagazineCollectionSerializer
    
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
                    'add_to_magazine_collection': is_logged,
                    'get_magazine_collection': is_logged,
                }
            }
        ),
    )

    @action(detail=False, url_path='add-to-magazine-collection', methods=['post'])
    def add_to_magazine_collection(self, request):
        userId = request.data['user']
        ammount = request.data['ammount']
        for magid in request.data['magazine']:
            magazine_user = User.objects.get(pk= userId)
            balance = magazine_user.balance
            balance -= float(ammount)
            magazine_user.balance = balance
            magazine_user.save()
            magazine_object = Magazine.objects.get(pk= magid)
            collection = MagazineCollection()
            collection.user = magazine_user
            collection.magazine = magazine_object
            collection.save()

        return Response({
            'status': 'Buyed Magazines Succesfully'
        })

    @action(detail=False, url_path='get-magazine-collection', methods=['get'])
    def get_magazine_collection(self, request):
        userId = request.query_params['user']
        user = User.objects.get(pk = userId)
        magazines = MagazineCollection.objects.filter(user = user)
        collection = MagazineCollectionSerializer(magazines, many = True).data
        return Response(collection)
