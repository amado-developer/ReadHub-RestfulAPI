from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Log
from .serializers import LogSerializer
from rest_framework.response import Response
class LogViewset(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    @action(detail=False, url_path='get-log', methods=['get'])
    def get_log(self, request):
        user_id = request.query_params['user']
        log = Log.objects.filter(user=user_id)
        
        return Response(LogSerializer(log, many=True).data)


