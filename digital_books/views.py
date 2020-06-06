from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from digital_books.models import Digital_Book
from digital_books.serializers import digital_bookSerializer
from adquisitions.models import Collection
from rest_framework.response import Response
from django.http.request import QueryDict
from rest_framework.utils import json
from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email

class digital_bookViewSet(viewsets.ModelViewSet):
    queryset = Digital_Book.objects.all()
    serializer_class = digital_bookSerializer

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
                    'rate': is_logged
                }
            }
        ),
    )

    @action(detail=False ,methods=['get'])
    def search(self, request):
        search_filter = request.query_params['bookName']
        user = request.query_params['user']
        books = Digital_Book.objects.filter(name__contains= search_filter)
        users_current_books= Collection.objects.filter(user=user).values()
        books_list = list(books)
        collection = list(users_current_books)
        filtered_books_list = []
        for book in books_list:
            for b in collection:
                if b['book_id'] == book.id:
                    filtered_books_list.append(book)

        for book in filtered_books_list:
            books_list.remove(book)

        books_response = digital_bookSerializer(books_list, many = True).data
        return Response(books_response)
        
    @action(detail=True, methods=['patch', 'put'])
    def rate(self, request, pk=None):
        rating = request.query_params['rating']
        book = self.get_object()
        current_rating = book.rating
        if current_rating > 0:
            new_rating =  (float(current_rating) + float(rating))/2
            book.rating = new_rating
            book.save()
        else:
            new_rating = rating
            book.rating = new_rating
            book.save()
        return Response(digital_bookSerializer(book).data)

   
    

