from rest_framework import serializers
from studyclassrooms.models import StudyClassrooom


class StudyClassrooomSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyClassrooom
        fields = (
            'id',
            'number',   
        )
