from django.shortcuts import render
from magazines.serializers import MagazinesSerializer
from rest_framework import viewsets
from magazines.models import Magazine
from rest_framework.response import Response
from rest_framework.decorators import action
# Create your views here.

class MagazineViewSet(viewsets.ModelViewSet):
    queryset = Magazine.objects.all()
    serializer_class = MagazinesSerializer

    @action(detail=False ,methods=['get'],url_path='get-magazine-collection')
    def search(self, request):
        search_filter = request.query_params['magazineName']
        magazines = Magazine.objects.filter(name__contains= search_filter)
        magazines_response = MagazinesSerializer(magazines, many = True).data
        return Response(magazines_response)
        
