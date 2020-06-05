from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Collection
from .serializers import CollectionSerializer
from users.models import User
from users.serializers import UserSerializer
from digital_books.models import Digital_Book
from digital_books.serializers import digital_bookSerializer
from django.http.response import JsonResponse
import json
from permissions.services import APIPermissionClassFactory

def is_logged(user, obj, request):
    return user.email == obj.email

class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': True,
                    'list': False,
                },
                'instance': {
                    'retrieve': False,
                    'destroy': False,
                    'update': False,
                    'add_to_collection': is_logged,
                    'get_collection' : is_logged,
                }
            }
        ),
    )

    @action(detail=False, url_path='add-to-collection', methods=['post'])
    def add_to_collection(self, request):
        userId = request.data['user']
        ammount = request.data['ammount']
        for bookId in request.data['books']:
            book_user = User.objects.get(pk= userId)
            balance = book_user.balance
            balance -= ammount
            book_user.balance = balance
            book_user.save()
            book_object = Digital_Book.objects.get(pk= bookId)
            collection = Collection()
            collection.user = book_user
            collection.book = book_object
            collection.save()

        return Response({
            'status': 'Buyed Succesfully'
        })

    @action(detail=False, url_path='get-collection', methods=['get'])
    def get_collection(self, request):
        books_array = []
        response = []
        userId = request.query_params['user']
        user = User.objects.get(pk = userId)
        books = Collection.objects.filter(user = user)
        # books_serialized = digital_bookSerializer(books, many=True).data
        collection = CollectionSerializer(books, many = True).data
        print(collection)
        return Response(collection)
    
    

