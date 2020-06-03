from rest_framework import serializers
from studyclassrooms_reservations.models import StudyClassrooms_Reservation


class StudyClassroom_ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyClassrooms_Reservation
        fields = (
            'id',
            'user',
            'study_classroom',
            'loan_date',
            'devolution_date',
        )




