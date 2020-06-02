from rest_framework import serializers
from .models import Log

'''

activity
datetime
user (FK)
type


'''
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = (
            'id',
            'activity',
            'datetime',
            'user'
        )