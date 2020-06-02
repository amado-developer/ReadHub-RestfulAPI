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

class MagazineCollectionViewset(viewsets.ModelViewSet):
    queryset = MagazineCollection.objects.all()
    serializer_class = MagazineCollectionSerializer
    
    @action(detail=False, url_path='add-to-magazine-collection', methods=['post'])
    def add_to_magazine_collection(self, request):
        userId = request.data['user']
        for magid in request.data['magazine']:
            magazine_user = User.objects.get(pk= userId)
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
        print(collection)
        return Response(collection)
