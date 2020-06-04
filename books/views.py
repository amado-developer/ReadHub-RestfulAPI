from django.shortcuts import render
from rest_framework import viewsets

from books.models import Book
from books.serializers import BookSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    @action(detail=False ,methods=['get'])
    def search(self, request):
        search_filter = request.query_params['bookName']
        books = Book.objects.filter(name__contains= search_filter)
        books_response = BookSerializer(books, many = True).data
        return Response(books_response)