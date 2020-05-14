from django.shortcuts import render
from rest_framework import viewsets
from digital_books.models import digital_book
from digital_books.serializers import digital_bookSerializer


class digital_bookViewSet(viewsets.ModelViewSet):
    queryset = digital_book.objects.all()
    serializer_class = digital_bookSerializer
