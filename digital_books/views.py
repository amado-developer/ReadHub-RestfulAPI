from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from digital_books.models import Digital_Book
from digital_books.serializers import digital_bookSerializer
from rest_framework.response import Response
from django.http.request import QueryDict
from rest_framework.utils import json


class digital_bookViewSet(viewsets.ModelViewSet):
    queryset = Digital_Book.objects.all()
    serializer_class = digital_bookSerializer


    @action(detail=False ,methods=['get'])
    def search(self, request):
        search_filter = request.query_params['bookName']
        
        books = Digital_Book.objects.filter(name__contains= search_filter)
        books_response = digital_bookSerializer(books, many = True).data
        return Response(books_response)
        


