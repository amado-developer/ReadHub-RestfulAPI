from django.shortcuts import render
from rest_framework import viewsets
from audio_books.models import Audio_Book
from audio_books.serializers import Audio_BookSerializer


class Audio_BookViewSet(viewsets.ModelViewSet):
    queryset = Audio_Book.objects.all()
    serializer_class = Audio_BookSerializer

