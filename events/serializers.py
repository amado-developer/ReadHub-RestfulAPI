from rest_framework import serializers
from .models import Event

'''
description
type
datetime

'''
class EventSerializer(serializers.ModelSerializer):
    model = Event
    fields = (
        'id',
        'type',
        'description',
        'datetime'
    )