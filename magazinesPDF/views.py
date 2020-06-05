from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import MagazinePDFSerializer
from .models import MagazinesPDF
from users.models import User
from users.serializers import UserSerializer
from magazines.models import Magazine
from magazinecollections.models import MagazineCollection
from magazinecollections.serializers import MagazineCollectionSerializer

from permissions.services import APIPermissionClassFactory

def is_admin(user, request):
    return user.is_admin == True

def is_logged(user, obj, request):
    return user.email == obj.email

class MagazinePDFViewSet(viewsets.ModelViewSet):
    queryset = MagazinesPDF.objects.all()
    serializer_class = MagazinePDFSerializer

    permission_classes = (
        APIPermissionClassFactory(
            name='UserPermission',
            permission_configuration={
                'base': {
                    'create': is_admin,
                    'list': True,
                },
                'instance': {
                    'retrieve': is_logged,
                    'destroy': False,
                    'update': False,
                    'get_magazine_pdf': is_logged,
                }
            }
        ),
    )

    @action(detail=False, url_path='get-magazine-pdf', methods=['get'])
    def get_magazine_pdf(self, request):
        user_id = request.query_params['user']
        user = User.objects.get(pk=user_id)
        collection = MagazineCollection.objects.filter(user=user)
        pdf = []
        for magazine in collection:
             try:
                 magazinespdf = MagazinesPDF.objects.get(magazine=magazine.magazine)
                 pdf.append(MagazinePDFSerializer(magazinespdf).data)
           
             except MagazinesPDF.DoesNotExist:
                pass
       
        return Response(pdf)
    