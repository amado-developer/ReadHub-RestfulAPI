from django.shortcuts import render
from rest_framework import viewsets

from authors.models import Author
from authors.serializers import AuthorSerializer

class AuthorsViewSets(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer