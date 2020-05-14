from django.shortcuts import render
from studyclassrooms_reservations.models import StudyClassrooms_Reservation
from studyclassrooms_reservations.serializers import StudyClassroom_ReservationSerializer
from rest_framework import viewsets


class StudyClassrooms_ReservationViewSet(viewsets.ModelViewSet):
    queryset = StudyClassrooms_Reservation.objects.all()
    serializer_class = StudyClassroom_ReservationSerializer

