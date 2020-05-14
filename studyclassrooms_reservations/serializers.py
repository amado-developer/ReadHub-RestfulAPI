from rest_framework import serializers
from studyclassrooms_reservations.models import StudyClassrooms_Reservation


class StudyClassroom_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyClassrooms_Reservation
        fiels = (
            'id',
            'User',
            'study_classroom',
            'enter_hour',
            'return_hour',
        )




