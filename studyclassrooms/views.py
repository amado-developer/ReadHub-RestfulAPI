from django.shortcuts import render
from rest_framework import viewsets
from studyclassrooms.models import StudyClassrooom
from studyclassrooms.serializers import StudyClassrooomSerializer

class StudyClassrooomViewSets(viewsets.ModelViewSet):
    queryset = StudyClassrooom.objects.all()
    serializer_class = StudyClassrooomSerializer





