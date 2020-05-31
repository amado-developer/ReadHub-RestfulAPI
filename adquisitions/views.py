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

class CollectionViewset(viewsets.ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer


    @action(detail=False, url_path='add-to-collection', methods=['post'])
    def add_to_collection(self, request):
        userId = request.data['user']
        for bookId in request.data['books']:
            book_user = User.objects.get(pk= userId)
            book_user.save()
            book_object = Digital_Book.objects.get(pk= bookId)
            collection = Collection()
            collection.user = book_user
            collection.book = book_object
            collection.save()

        return Response({
            'status': 'Buyed Succesfully'
        })
    

